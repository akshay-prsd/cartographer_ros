#!/usr/bin/env python

import time
import rospy
import rosbag
import os
import subprocess
import argparse
import signal
import sys
from rosgraph_msgs import msg
import roslaunch
from cartographer_ros_msgs.srv import WriteState
from cartographer_ros_msgs.srv import FinishTrajectory
from collections import defaultdict

global current_time
import exceptions

global roscore_process


def signal_handler(sig, frame):
    roscore_process.send_signal(subprocess.signal.SIGTERM)
    roscore_process.wait()
    sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-od", "--output_dir", type=str,
                        help="Full path of output directory, default: ./bnr_cartographer_output",
                        default=os.getcwd() + "/bnr_cartographer_output/")
    parser.add_argument("-cfi", "--cart_config_file", type=str, help="Cartographer config filename, default: atlas.lua",
                        default="atlas.lua")
    parser.add_argument("-clf", "--cart_launch_file", type=str,
                        help="Cartographer ROS launch file, default: atlas_online_2d.launch",
                        default="atlas_online_2d.launch")
    parser.add_argument_group("Required name arguments")
    parser.add_argument("-bd", "--bag_dir", type=str, help="Root directory where BNR shelf bags can be found",
                        required=True)
    parser.add_argument("-cfo", "--cart_config_folder", type=str, help="Full path of Cartographer config folder",
                        required=True)

    args = parser.parse_args()

    roscore_process = subprocess.Popen('roscore')
    rospy.init_node("cart_player")
    work_path = args.bag_dir
    output_path = args.output_dir
    cart_config_file = args.cart_config_file
    cart_config_folder = args.cart_config_folder
    cart_launch_file = args.cart_launch_file
    signal.signal(signal.SIGINT, signal_handler)

    bag_dirs = defaultdict(list)

    save_cartographer_state = rospy.ServiceProxy('/write_state', WriteState)
    finish_trajectory = rospy.ServiceProxy('/finish_trajectory', FinishTrajectory)
    # start_trajectory = rospy.ServiceProxy('/start_trajectory', StartTrajectory)

    for root, dirs, files in os.walk(work_path):
        for name in files:
            if "bag" in name and "pbstream" not in name:
                bag_dirs[root].append(name)
    print  bag_dirs

    for bag_dir, bags in bag_dirs.iteritems():
        print bags
        print os.path.join(output_path , os.path.split(bag_dir)[1])
        if not os.path.isdir(os.path.join(output_path , os.path.split(bag_dir)[1])):
            try:
                os.makedirs(os.path.join(output_path , os.path.split(bag_dir)[1]))
                print output_path + os.path.split(bag_dir)[1]
            except OSError as e:
                print ("Unable to make directory, please provide clean output dir")
                roscore_process.send_signal(subprocess.signal.SIGTERM)
                sys.exit(-1)
        print ['roslaunch', 'cartographer_ros', cart_launch_file,
                                                 'config_folder:=' + cart_config_folder,
                                                 'config_file:=' + cart_config_file]
        cartographer_process = subprocess.Popen(['roslaunch', 'cartographer_ros', cart_launch_file,
                                                 'config_folder:=' + cart_config_folder,
                                                 'config_file:=' + cart_config_file])
        rospy.wait_for_service('/write_state')
        bag_list = []
        for bag in sorted(bags):
            bag_list.append(os.path.join(bag_dir, bag))
        print bag_list
        robag_process = subprocess.Popen(['rosbag', 'play', '--clock'] + bag_list)
        robag_process.wait()
        time.sleep(120)
        finish_trajectory(0)
        print str(os.path.join(output_path,  bags[0] + '.pbstream'))
        save_cartographer_state(str(os.path.join(output_path , bags[0] + '.pbstream')), bool('true') )
        time.sleep(120)
        cartographer_process.send_signal(subprocess.signal.SIGTERM)
        cartographer_process.wait()
        print ['roslaunch', 'cartographer_ros', 'assets_writer_ros_map.launch',
         'bag_filenames:=' + " ".join(bag_list),
         'pose_graph_filename:=' + str(os.path.join(output_path, bags[0] + '.pbstream'))]
        asset_writer_process = subprocess.Popen(
            ['roslaunch', 'cartographer_ros', 'assets_writer_ros_map.launch',
             'bag_filenames:=' + " ".join(bag_list),
             'pose_graph_filename:=' + str(os.path.join(output_path, bags[0] + '.pbstream'))])
        asset_writer_process.wait()

    roscore_process.send_signal(subprocess.signal.SIGTERM)
    roscore_process.wait()

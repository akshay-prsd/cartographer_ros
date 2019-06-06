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
    parser.add_argument("-bag", "--bag", type=str, help="BNR shelf bags can be found")
    parser.add_argument("-pbstream", "--pbstream", type=str, help="BNR pbstream bags can be found", required=True)
    parser.add_argument("-cfo", "--cart_config_folder", type=str, help="Full path of Cartographer config folder",
                        required=True)

    args = parser.parse_args()

    
    rospy.init_node("cart_player")
    finish_trajectory = rospy.ServiceProxy('/finish_trajectory', FinishTrajectory)
    save_cartographer_state = rospy.ServiceProxy('/write_state', WriteState)
    bag_path = args.bag
    cart_config_file = args.cart_config_file
    cart_config_folder = args.cart_config_folder
    cart_launch_file = args.cart_launch_file
    pbstream_data = args.pbstream
    signal.signal(signal.SIGINT, signal_handler)


    print ['roslaunch', 'cartographer_ros', cart_launch_file,
                                             'config_folder:=' + cart_config_folder,
                                             'config_file:=' + cart_config_file]
    cartographer_process = subprocess.Popen(['roslaunch', 'cartographer_ros', cart_launch_file,
                                             'config_folder:=' + cart_config_folder,
                                             'config_file:=' + cart_config_file,
                                             'load_state_filename:=' + pbstream_data])
    
    
    time.sleep(60) 
    finish_trajectory(9)
    command = ['rosrun', 'cartographer_ros', 'cartographer_start_trajectory',
            '-configuration_directory', cart_config_folder,
            '-configuration_basename', cart_config_file,
            '-initial_pose', '{to_trajectory_id =' + str(0) +', relative_pose = { translation = { 10.3728, -13.5311, 0. }, rotation = { 0.0, 0.0, -1.6430 } }, time = 0 }']
    
    # command = ['rosrun', 'cartographer_ros', 'cartographer_start_trajectory',
    #         '-configuration_directory', cart_config_folder,
    #         '-configuration_basename', cart_config_file,
    #         '-initial_pose', '{to_trajectory_id =' + str(0) +', relative_pose = { translation = { 0, 0, 0. }, rotation = { 0.0, 0.0, 0.0 } }, time = 0 }']        
    start_trajectory_process = subprocess.Popen(command)
    time.sleep(30)   
    robag_process = subprocess.Popen(['rosbag', 'play', '--clock'] + [bag_path])
    robag_process.wait()
    finish_trajectory(10)
    print str(os.path.join(bag_path,  'localization' + '.pbstream'))
    save_cartographer_state(str(os.path.join(bag_path , 'localization' + '.pbstream')), bool('true') ) 
    time.sleep(60)   
    cartographer_process.send_signal(subprocess.signal.SIGTERM)
    cartographer_process.wait()


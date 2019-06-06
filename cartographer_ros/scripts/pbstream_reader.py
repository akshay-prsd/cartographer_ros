#!/usr/bin/env python

import os
import sys
import gzip
import struct
import numpy as np
import zlib
import cartographer.mapping
# import cartographer.mapping.proto.sparse_pose_graph_pb2
# import cartographer.mapping.proto.serialization_pb2
import matplotlib.pyplot as plt

def pbstreamreader(posefile):
    print "Reading .pbstream data"
    idnumber = '0x7b1d1f7b5bf501db'
    filehandle = open(posefile, 'rb')
    # make sure the data
    size = readthefile(filehandle)
    if idnumber!= size:
        print "unknown string"
        return

    #get the total size of the data
    size = readsize(filehandle)
    #print  size
    compressed_trajectory_data = readdatafromfile(filehandle,int(size))

    trajectory_data = zlib.decompress(compressed_trajectory_data,16+zlib.MAX_WBITS)

    # read the entire data of the file
    pose_graph=sparse_pose_graph_pb2.SparsePoseGraph()
    pose_graph.ParseFromString(trajectory_data)
    maptoddler_trajectory = []
    #print len(pose_graph.trajectory)
    for i in xrange(0,len(pose_graph.trajectory)):
        for j in xrange(0,len(pose_graph.trajectory[i].node)):
            maptoddler_trajectory.append(pose_graph.trajectory[i].node[j])

    plot_poses(maptoddler_trajectory)

    filehandle.close()
    return maptoddler_trajectory

def plot_poses(trajectory):

    x = []
    y = []

    for i in xrange(0,len(trajectory)):
        x.append(trajectory[i].pose.translation.x)
        y.append(trajectory[i].pose.translation.y)

    print len(x)
    print len(y)
    plt.plot(x,y,'r.')
    plt.axis([min(x), max(x), min(y), max(y)])
    plt.show()


def readthefile(fileobj):
    size =0
    byte=None
    word = []
    for i in range(0,8):
        byte = fileobj.read(1).encode("hex")
        word.append(byte)
    word = word[::-1]
    word = '0x'+''.join(word)
    return word
def readsize(fileobj):
    return struct.unpack_from("<Q", fileobj.read(8))[0]

def readdatafromfile(fileobj, size):
    return fileobj.read(size)

def main():
    if len(sys.argv)!=2:
        print "Incorrect usage. rosrun maptoddlerpostprocessing generateassetsfrombag.py <path/to/the/*.pbstream>"
        return
    trajectory = pbstreamreader(sys.argv[1])

if __name__=='__main__':
    main()

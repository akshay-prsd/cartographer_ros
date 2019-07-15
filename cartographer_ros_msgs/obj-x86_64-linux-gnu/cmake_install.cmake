# Install script for directory: /home/akshay/src/cartographer_ros/cartographer_ros_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/opt/ros/kinetic")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "None")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cartographer_ros_msgs/msg" TYPE FILE FILES
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/msg/BagfileProgress.msg"
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/msg/HistogramBucket.msg"
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/msg/LandmarkEntry.msg"
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/msg/LandmarkList.msg"
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/msg/MetricFamily.msg"
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/msg/MetricLabel.msg"
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/msg/Metric.msg"
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/msg/StatusCode.msg"
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/msg/StatusResponse.msg"
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/msg/SubmapEntry.msg"
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/msg/SubmapList.msg"
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/msg/SubmapTexture.msg"
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/msg/TrajectoryStates.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cartographer_ros_msgs/srv" TYPE FILE FILES
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/srv/FinishTrajectory.srv"
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/srv/GetTrajectoryStates.srv"
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/srv/ReadMetrics.srv"
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/srv/StartTrajectory.srv"
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/srv/SubmapQuery.srv"
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/srv/TrajectoryQuery.srv"
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/srv/WriteState.srv"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cartographer_ros_msgs/cmake" TYPE FILE FILES "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/obj-x86_64-linux-gnu/catkin_generated/installspace/cartographer_ros_msgs-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/obj-x86_64-linux-gnu/devel/include/cartographer_ros_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/obj-x86_64-linux-gnu/devel/share/roseus/ros/cartographer_ros_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/obj-x86_64-linux-gnu/devel/share/common-lisp/ros/cartographer_ros_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/obj-x86_64-linux-gnu/devel/share/gennodejs/ros/cartographer_ros_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/obj-x86_64-linux-gnu/devel/lib/python2.7/dist-packages/cartographer_ros_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/obj-x86_64-linux-gnu/devel/lib/python2.7/dist-packages/cartographer_ros_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/obj-x86_64-linux-gnu/catkin_generated/installspace/cartographer_ros_msgs.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cartographer_ros_msgs/cmake" TYPE FILE FILES "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/obj-x86_64-linux-gnu/catkin_generated/installspace/cartographer_ros_msgs-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cartographer_ros_msgs/cmake" TYPE FILE FILES
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/obj-x86_64-linux-gnu/catkin_generated/installspace/cartographer_ros_msgsConfig.cmake"
    "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/obj-x86_64-linux-gnu/catkin_generated/installspace/cartographer_ros_msgsConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cartographer_ros_msgs" TYPE FILE FILES "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/package.xml")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/akshay/src/cartographer_ros/cartographer_ros_msgs/obj-x86_64-linux-gnu/gtest/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/akshay/src/cartographer_ros/cartographer_ros_msgs/obj-x86_64-linux-gnu/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")

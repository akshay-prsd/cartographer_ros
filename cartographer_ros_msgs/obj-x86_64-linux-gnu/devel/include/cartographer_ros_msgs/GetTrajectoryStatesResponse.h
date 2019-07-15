// Generated by gencpp from file cartographer_ros_msgs/GetTrajectoryStatesResponse.msg
// DO NOT EDIT!


#ifndef CARTOGRAPHER_ROS_MSGS_MESSAGE_GETTRAJECTORYSTATESRESPONSE_H
#define CARTOGRAPHER_ROS_MSGS_MESSAGE_GETTRAJECTORYSTATESRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <cartographer_ros_msgs/StatusResponse.h>
#include <cartographer_ros_msgs/TrajectoryStates.h>

namespace cartographer_ros_msgs
{
template <class ContainerAllocator>
struct GetTrajectoryStatesResponse_
{
  typedef GetTrajectoryStatesResponse_<ContainerAllocator> Type;

  GetTrajectoryStatesResponse_()
    : status()
    , trajectory_states()  {
    }
  GetTrajectoryStatesResponse_(const ContainerAllocator& _alloc)
    : status(_alloc)
    , trajectory_states(_alloc)  {
  (void)_alloc;
    }



   typedef  ::cartographer_ros_msgs::StatusResponse_<ContainerAllocator>  _status_type;
  _status_type status;

   typedef  ::cartographer_ros_msgs::TrajectoryStates_<ContainerAllocator>  _trajectory_states_type;
  _trajectory_states_type trajectory_states;





  typedef boost::shared_ptr< ::cartographer_ros_msgs::GetTrajectoryStatesResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::cartographer_ros_msgs::GetTrajectoryStatesResponse_<ContainerAllocator> const> ConstPtr;

}; // struct GetTrajectoryStatesResponse_

typedef ::cartographer_ros_msgs::GetTrajectoryStatesResponse_<std::allocator<void> > GetTrajectoryStatesResponse;

typedef boost::shared_ptr< ::cartographer_ros_msgs::GetTrajectoryStatesResponse > GetTrajectoryStatesResponsePtr;
typedef boost::shared_ptr< ::cartographer_ros_msgs::GetTrajectoryStatesResponse const> GetTrajectoryStatesResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::cartographer_ros_msgs::GetTrajectoryStatesResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::cartographer_ros_msgs::GetTrajectoryStatesResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace cartographer_ros_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'cartographer_ros_msgs': ['/home/akshay/src/cartographer_ros/cartographer_ros_msgs/msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::cartographer_ros_msgs::GetTrajectoryStatesResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::cartographer_ros_msgs::GetTrajectoryStatesResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cartographer_ros_msgs::GetTrajectoryStatesResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cartographer_ros_msgs::GetTrajectoryStatesResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cartographer_ros_msgs::GetTrajectoryStatesResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cartographer_ros_msgs::GetTrajectoryStatesResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::cartographer_ros_msgs::GetTrajectoryStatesResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b9e3b373f17df088ee6dcd817b79dff0";
  }

  static const char* value(const ::cartographer_ros_msgs::GetTrajectoryStatesResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb9e3b373f17df088ULL;
  static const uint64_t static_value2 = 0xee6dcd817b79dff0ULL;
};

template<class ContainerAllocator>
struct DataType< ::cartographer_ros_msgs::GetTrajectoryStatesResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cartographer_ros_msgs/GetTrajectoryStatesResponse";
  }

  static const char* value(const ::cartographer_ros_msgs::GetTrajectoryStatesResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::cartographer_ros_msgs::GetTrajectoryStatesResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cartographer_ros_msgs/StatusResponse status\n\
cartographer_ros_msgs/TrajectoryStates trajectory_states\n\
\n\
\n\
================================================================================\n\
MSG: cartographer_ros_msgs/StatusResponse\n\
# Copyright 2018 The Cartographer Authors\n\
#\n\
# Licensed under the Apache License, Version 2.0 (the \"License\");\n\
# you may not use this file except in compliance with the License.\n\
# You may obtain a copy of the License at\n\
#\n\
#      http://www.apache.org/licenses/LICENSE-2.0\n\
#\n\
# Unless required by applicable law or agreed to in writing, software\n\
# distributed under the License is distributed on an \"AS IS\" BASIS,\n\
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n\
# See the License for the specific language governing permissions and\n\
# limitations under the License.\n\
\n\
# A common message type to indicate the outcome of a service call.\n\
uint8 code\n\
string message\n\
\n\
================================================================================\n\
MSG: cartographer_ros_msgs/TrajectoryStates\n\
# Copyright 2018 The Cartographer Authors\n\
#\n\
# Licensed under the Apache License, Version 2.0 (the 'License');\n\
# you may not use this file except in compliance with the License.\n\
# You may obtain a copy of the License at\n\
#\n\
#      http://www.apache.org/licenses/LICENSE-2.0\n\
#\n\
# Unless required by applicable law or agreed to in writing, software\n\
# distributed under the License is distributed on an 'AS IS' BASIS,\n\
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n\
# See the License for the specific language governing permissions and\n\
# limitations under the License.\n\
\n\
uint8 ACTIVE = 0\n\
uint8 FINISHED = 1\n\
uint8 FROZEN = 2\n\
uint8 DELETED = 3\n\
\n\
std_msgs/Header header\n\
int32[] trajectory_id\n\
uint8[] trajectory_state\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
";
  }

  static const char* value(const ::cartographer_ros_msgs::GetTrajectoryStatesResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::cartographer_ros_msgs::GetTrajectoryStatesResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.status);
      stream.next(m.trajectory_states);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GetTrajectoryStatesResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::cartographer_ros_msgs::GetTrajectoryStatesResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::cartographer_ros_msgs::GetTrajectoryStatesResponse_<ContainerAllocator>& v)
  {
    s << indent << "status: ";
    s << std::endl;
    Printer< ::cartographer_ros_msgs::StatusResponse_<ContainerAllocator> >::stream(s, indent + "  ", v.status);
    s << indent << "trajectory_states: ";
    s << std::endl;
    Printer< ::cartographer_ros_msgs::TrajectoryStates_<ContainerAllocator> >::stream(s, indent + "  ", v.trajectory_states);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CARTOGRAPHER_ROS_MSGS_MESSAGE_GETTRAJECTORYSTATESRESPONSE_H

// Generated by gencpp from file cartographer_ros_msgs/TrajectoryQueryRequest.msg
// DO NOT EDIT!


#ifndef CARTOGRAPHER_ROS_MSGS_MESSAGE_TRAJECTORYQUERYREQUEST_H
#define CARTOGRAPHER_ROS_MSGS_MESSAGE_TRAJECTORYQUERYREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace cartographer_ros_msgs
{
template <class ContainerAllocator>
struct TrajectoryQueryRequest_
{
  typedef TrajectoryQueryRequest_<ContainerAllocator> Type;

  TrajectoryQueryRequest_()
    : trajectory_id(0)  {
    }
  TrajectoryQueryRequest_(const ContainerAllocator& _alloc)
    : trajectory_id(0)  {
  (void)_alloc;
    }



   typedef int32_t _trajectory_id_type;
  _trajectory_id_type trajectory_id;





  typedef boost::shared_ptr< ::cartographer_ros_msgs::TrajectoryQueryRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::cartographer_ros_msgs::TrajectoryQueryRequest_<ContainerAllocator> const> ConstPtr;

}; // struct TrajectoryQueryRequest_

typedef ::cartographer_ros_msgs::TrajectoryQueryRequest_<std::allocator<void> > TrajectoryQueryRequest;

typedef boost::shared_ptr< ::cartographer_ros_msgs::TrajectoryQueryRequest > TrajectoryQueryRequestPtr;
typedef boost::shared_ptr< ::cartographer_ros_msgs::TrajectoryQueryRequest const> TrajectoryQueryRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::cartographer_ros_msgs::TrajectoryQueryRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::cartographer_ros_msgs::TrajectoryQueryRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace cartographer_ros_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'cartographer_ros_msgs': ['/home/akshay/src/cartographer_ros/cartographer_ros_msgs/msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::cartographer_ros_msgs::TrajectoryQueryRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::cartographer_ros_msgs::TrajectoryQueryRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cartographer_ros_msgs::TrajectoryQueryRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cartographer_ros_msgs::TrajectoryQueryRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cartographer_ros_msgs::TrajectoryQueryRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cartographer_ros_msgs::TrajectoryQueryRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::cartographer_ros_msgs::TrajectoryQueryRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6e190c4be941828bcd09ea05053f4bb5";
  }

  static const char* value(const ::cartographer_ros_msgs::TrajectoryQueryRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6e190c4be941828bULL;
  static const uint64_t static_value2 = 0xcd09ea05053f4bb5ULL;
};

template<class ContainerAllocator>
struct DataType< ::cartographer_ros_msgs::TrajectoryQueryRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cartographer_ros_msgs/TrajectoryQueryRequest";
  }

  static const char* value(const ::cartographer_ros_msgs::TrajectoryQueryRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::cartographer_ros_msgs::TrajectoryQueryRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
int32 trajectory_id\n\
";
  }

  static const char* value(const ::cartographer_ros_msgs::TrajectoryQueryRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::cartographer_ros_msgs::TrajectoryQueryRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.trajectory_id);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct TrajectoryQueryRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::cartographer_ros_msgs::TrajectoryQueryRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::cartographer_ros_msgs::TrajectoryQueryRequest_<ContainerAllocator>& v)
  {
    s << indent << "trajectory_id: ";
    Printer<int32_t>::stream(s, indent + "  ", v.trajectory_id);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CARTOGRAPHER_ROS_MSGS_MESSAGE_TRAJECTORYQUERYREQUEST_H

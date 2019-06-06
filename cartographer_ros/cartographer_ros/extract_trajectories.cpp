#include "cartographer/io/proto_stream.h"
#include "cartographer/io/proto_stream_deserializer.h"
#include "cartographer/mapping/pose_graph.h"
#include "cartographer_ros/msg_conversion.h"
#include "cartographer_ros/time_conversion.h"
#include "geometry_msgs/TransformStamped.h"
#include <iostream>
#include <fstream>
using namespace std;

namespace cartographer_ros {

namespace carto = ::cartographer;

void ExportPbstream(const std::string& pbstream_filename, ofstream& submap_txt, ofstream& constraint_txt, ofstream& trajectory_txt) {
  carto::io::ProtoStreamReader reader(pbstream_filename);
  carto::io::ProtoStreamDeserializer deserializer(&reader);

  carto::mapping::proto::PoseGraph pose_graph_proto = deserializer.pose_graph();
  std::cout << pose_graph_proto.constraint().size() << std::endl;
  int constraint;
  for (size_t constraint_id = 0; constraint_id < pose_graph_proto.constraint().size(); ++constraint_id) {
    switch(pose_graph_proto.constraint(constraint_id).tag()) {
      case carto::mapping::proto::PoseGraph::Constraint::INTRA_SUBMAP:
        constraint = 0;
        break;
      case carto::mapping::proto::PoseGraph::Constraint::INTER_SUBMAP:
        constraint = 1;
        break;
    }
    constraint_txt << "trajectory_id " << pose_graph_proto.constraint(constraint_id).submap_id().trajectory_id() << " submap_index " <<
     pose_graph_proto.constraint(constraint_id).submap_id().submap_index() << " constraint " << constraint <<
     " trajectory_id "<< pose_graph_proto.constraint(constraint_id).node_id().trajectory_id() << " node_index " <<
     pose_graph_proto.constraint(constraint_id).node_id().node_index() << " translation_weight " <<
     pose_graph_proto.constraint(constraint_id).translation_weight() << " rotation_weight " <<
    pose_graph_proto.constraint(constraint_id).rotation_weight() << std::endl;
  }

  for (size_t trajectory_id = 0; trajectory_id < pose_graph_proto.trajectory().size();
       ++trajectory_id) {
    const carto::mapping::proto::Trajectory& trajectory_proto =
        pose_graph_proto.trajectory(trajectory_id);
    // std::cout << trajectory_proto.node_size() << std::endl;
    for (int i = 0; i < trajectory_proto.node_size(); ++i) {
      const auto& node = trajectory_proto.node(i);
      const auto& pose = node.pose();
       trajectory_txt << "trajectory_id " << trajectory_proto.trajectory_id() << " node_id " << node.node_index() <<
       " " << pose.translation().x() << " " << pose.translation().y() << std::endl;

    }
    for (int i = 0; i < trajectory_proto.submap_size(); ++i) {
      const auto& submap = trajectory_proto.submap(i);
      const auto& pose = submap.pose();
      submap_txt << "trajectory_id " << trajectory_proto.trajectory_id() << " submap_id " << submap.submap_index()
      << " " << pose.translation().x() << " " << pose.translation().y() << std::endl;
    }
  }
}
} // namespace

int main(int argc, char** argv) {
  ofstream submap_txt;
  ofstream constraint_txt;
  ofstream trajectory_txt;
  submap_txt.open("submap.txt");
  constraint_txt.open("constraint.txt");
  trajectory_txt.open("trajectory.txt");

  std::cout << argv[0] << std::endl;
  std::cout << argv[1] << std::endl;
  std::string pbstream_filename(argv[1]);
  cartographer_ros::ExportPbstream(argv[1], submap_txt, constraint_txt, trajectory_txt);

  submap_txt.close();
  constraint_txt.close();
  trajectory_txt.close();
  return 0;
}

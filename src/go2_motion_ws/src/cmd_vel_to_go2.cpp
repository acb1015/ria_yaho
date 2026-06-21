// Bridge Nav2 /cmd_vel (geometry_msgs/Twist) -> Unitree Go2 walking.
//
// Uses the unitree_sdk2 SportClient directly (its own DDS channel on the given
// network interface), so it does NOT depend on the ROS2 RMW matching the Go2.
// One process: rclcpp receives /cmd_vel (any RMW, e.g. FastDDS like Nav2), the
// SDK sends Move() straight to the robot. This sidesteps the FastDDS/CycloneDDS
// mismatch.
//
// Run:  ros2 run go2_motion_ws cmd_vel_to_go2 eno1
// SAFETY: the robot physically walks. Speeds are clamped; a watchdog stops the
// robot if /cmd_vel goes silent. Keep the area clear and the e-stop ready, and
// make sure the Go2 is standing in sport mode.

#include <algorithm>
#include <chrono>
#include <memory>
#include <string>

#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/twist.hpp>

#include <unitree/robot/channel/channel_factory.hpp>
#include <unitree/robot/go2/sport/sport_client.hpp>

using namespace std::chrono_literals;

class CmdVelToGo2 : public rclcpp::Node
{
public:
  CmdVelToGo2()
  : rclcpp::Node("cmd_vel_to_go2")
  {
    max_vx_ = declare_parameter<double>("max_vx", 2.0);
    max_vy_ = declare_parameter<double>("max_vy", 0
      .8);
    max_vyaw_ = declare_parameter<double>("max_vyaw", 0.8);
    timeout_ = declare_parameter<double>("timeout", 0.5);

    sport_.SetTimeout(10.0f);
    sport_.Init();

    sub_ = create_subscription<geometry_msgs::msg::Twist>(
      "/cmd_vel", 10,
      std::bind(&CmdVelToGo2::onCmd, this, std::placeholders::_1));
    last_ = now();
    timer_ = create_wall_timer(100ms, std::bind(&CmdVelToGo2::watchdog, this));
    RCLCPP_INFO(get_logger(),
      "cmd_vel -> Go2 Move bridge ready (limits vx=%.2f vy=%.2f vyaw=%.2f).",
      max_vx_, max_vy_, max_vyaw_);
  }

private:
  static double clamp(double v, double m) { return std::max(-m, std::min(m, v)); }

  void move(double vx, double vy, double vyaw) { sport_.Move(vx, vy, vyaw); }

  void onCmd(const geometry_msgs::msg::Twist::SharedPtr t)
  {
    move(clamp(t->linear.x, max_vx_),
         clamp(t->linear.y, max_vy_),
         clamp(t->angular.z, max_vyaw_));
    last_ = now();
  }

  void watchdog()
  {
    if ((now() - last_).seconds() > timeout_) {
      move(0.0, 0.0, 0.0);  // no fresh command -> stop
    }
  }

  double max_vx_, max_vy_, max_vyaw_, timeout_;
  unitree::robot::go2::SportClient sport_;
  rclcpp::Subscription<geometry_msgs::msg::Twist>::SharedPtr sub_;
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Time last_;
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);

  // network interface for the Go2 SDK channel (default eno1; or pass as 1st arg)
  std::string net = "eno1";
  auto args = rclcpp::remove_ros_arguments(argc, argv);
  if (args.size() >= 2) {
    net = args[1];
  }
  std::cout << "Go2 SDK ChannelFactory Init on interface: " << net << std::endl;
  unitree::robot::ChannelFactory::Instance()->Init(0, net);

  rclcpp::spin(std::make_shared<CmdVelToGo2>());
  rclcpp::shutdown();
  return 0;
}

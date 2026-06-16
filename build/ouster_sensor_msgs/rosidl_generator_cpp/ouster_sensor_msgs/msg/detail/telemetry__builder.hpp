// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ouster_sensor_msgs:msg/Telemetry.idl
// generated code does not contain a copyright notice

#ifndef OUSTER_SENSOR_MSGS__MSG__DETAIL__TELEMETRY__BUILDER_HPP_
#define OUSTER_SENSOR_MSGS__MSG__DETAIL__TELEMETRY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ouster_sensor_msgs/msg/detail/telemetry__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ouster_sensor_msgs
{

namespace msg
{

namespace builder
{

class Init_Telemetry_shot_limiting
{
public:
  explicit Init_Telemetry_shot_limiting(::ouster_sensor_msgs::msg::Telemetry & msg)
  : msg_(msg)
  {}
  ::ouster_sensor_msgs::msg::Telemetry shot_limiting(::ouster_sensor_msgs::msg::Telemetry::_shot_limiting_type arg)
  {
    msg_.shot_limiting = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ouster_sensor_msgs::msg::Telemetry msg_;
};

class Init_Telemetry_thermal_shutdown
{
public:
  explicit Init_Telemetry_thermal_shutdown(::ouster_sensor_msgs::msg::Telemetry & msg)
  : msg_(msg)
  {}
  Init_Telemetry_shot_limiting thermal_shutdown(::ouster_sensor_msgs::msg::Telemetry::_thermal_shutdown_type arg)
  {
    msg_.thermal_shutdown = std::move(arg);
    return Init_Telemetry_shot_limiting(msg_);
  }

private:
  ::ouster_sensor_msgs::msg::Telemetry msg_;
};

class Init_Telemetry_countdown_shot_limiting
{
public:
  explicit Init_Telemetry_countdown_shot_limiting(::ouster_sensor_msgs::msg::Telemetry & msg)
  : msg_(msg)
  {}
  Init_Telemetry_thermal_shutdown countdown_shot_limiting(::ouster_sensor_msgs::msg::Telemetry::_countdown_shot_limiting_type arg)
  {
    msg_.countdown_shot_limiting = std::move(arg);
    return Init_Telemetry_thermal_shutdown(msg_);
  }

private:
  ::ouster_sensor_msgs::msg::Telemetry msg_;
};

class Init_Telemetry_countdown_thermal_shutdown
{
public:
  explicit Init_Telemetry_countdown_thermal_shutdown(::ouster_sensor_msgs::msg::Telemetry & msg)
  : msg_(msg)
  {}
  Init_Telemetry_countdown_shot_limiting countdown_thermal_shutdown(::ouster_sensor_msgs::msg::Telemetry::_countdown_thermal_shutdown_type arg)
  {
    msg_.countdown_thermal_shutdown = std::move(arg);
    return Init_Telemetry_countdown_shot_limiting(msg_);
  }

private:
  ::ouster_sensor_msgs::msg::Telemetry msg_;
};

class Init_Telemetry_header
{
public:
  Init_Telemetry_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Telemetry_countdown_thermal_shutdown header(::ouster_sensor_msgs::msg::Telemetry::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Telemetry_countdown_thermal_shutdown(msg_);
  }

private:
  ::ouster_sensor_msgs::msg::Telemetry msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ouster_sensor_msgs::msg::Telemetry>()
{
  return ouster_sensor_msgs::msg::builder::Init_Telemetry_header();
}

}  // namespace ouster_sensor_msgs

#endif  // OUSTER_SENSOR_MSGS__MSG__DETAIL__TELEMETRY__BUILDER_HPP_

// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ouster_sensor_msgs:msg/Telemetry.idl
// generated code does not contain a copyright notice

#ifndef OUSTER_SENSOR_MSGS__MSG__DETAIL__TELEMETRY__TRAITS_HPP_
#define OUSTER_SENSOR_MSGS__MSG__DETAIL__TELEMETRY__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ouster_sensor_msgs/msg/detail/telemetry__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace ouster_sensor_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Telemetry & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: countdown_thermal_shutdown
  {
    out << "countdown_thermal_shutdown: ";
    rosidl_generator_traits::value_to_yaml(msg.countdown_thermal_shutdown, out);
    out << ", ";
  }

  // member: countdown_shot_limiting
  {
    out << "countdown_shot_limiting: ";
    rosidl_generator_traits::value_to_yaml(msg.countdown_shot_limiting, out);
    out << ", ";
  }

  // member: thermal_shutdown
  {
    out << "thermal_shutdown: ";
    rosidl_generator_traits::value_to_yaml(msg.thermal_shutdown, out);
    out << ", ";
  }

  // member: shot_limiting
  {
    out << "shot_limiting: ";
    rosidl_generator_traits::value_to_yaml(msg.shot_limiting, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Telemetry & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: countdown_thermal_shutdown
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "countdown_thermal_shutdown: ";
    rosidl_generator_traits::value_to_yaml(msg.countdown_thermal_shutdown, out);
    out << "\n";
  }

  // member: countdown_shot_limiting
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "countdown_shot_limiting: ";
    rosidl_generator_traits::value_to_yaml(msg.countdown_shot_limiting, out);
    out << "\n";
  }

  // member: thermal_shutdown
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "thermal_shutdown: ";
    rosidl_generator_traits::value_to_yaml(msg.thermal_shutdown, out);
    out << "\n";
  }

  // member: shot_limiting
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "shot_limiting: ";
    rosidl_generator_traits::value_to_yaml(msg.shot_limiting, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Telemetry & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace ouster_sensor_msgs

namespace rosidl_generator_traits
{

[[deprecated("use ouster_sensor_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ouster_sensor_msgs::msg::Telemetry & msg,
  std::ostream & out, size_t indentation = 0)
{
  ouster_sensor_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ouster_sensor_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const ouster_sensor_msgs::msg::Telemetry & msg)
{
  return ouster_sensor_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<ouster_sensor_msgs::msg::Telemetry>()
{
  return "ouster_sensor_msgs::msg::Telemetry";
}

template<>
inline const char * name<ouster_sensor_msgs::msg::Telemetry>()
{
  return "ouster_sensor_msgs/msg/Telemetry";
}

template<>
struct has_fixed_size<ouster_sensor_msgs::msg::Telemetry>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<ouster_sensor_msgs::msg::Telemetry>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<ouster_sensor_msgs::msg::Telemetry>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // OUSTER_SENSOR_MSGS__MSG__DETAIL__TELEMETRY__TRAITS_HPP_

// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ouster_sensor_msgs:msg/Telemetry.idl
// generated code does not contain a copyright notice

#ifndef OUSTER_SENSOR_MSGS__MSG__DETAIL__TELEMETRY__STRUCT_HPP_
#define OUSTER_SENSOR_MSGS__MSG__DETAIL__TELEMETRY__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ouster_sensor_msgs__msg__Telemetry __attribute__((deprecated))
#else
# define DEPRECATED__ouster_sensor_msgs__msg__Telemetry __declspec(deprecated)
#endif

namespace ouster_sensor_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Telemetry_
{
  using Type = Telemetry_<ContainerAllocator>;

  explicit Telemetry_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->countdown_thermal_shutdown = 0;
      this->countdown_shot_limiting = 0;
      this->thermal_shutdown = 0;
      this->shot_limiting = 0;
    }
  }

  explicit Telemetry_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->countdown_thermal_shutdown = 0;
      this->countdown_shot_limiting = 0;
      this->thermal_shutdown = 0;
      this->shot_limiting = 0;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _countdown_thermal_shutdown_type =
    uint16_t;
  _countdown_thermal_shutdown_type countdown_thermal_shutdown;
  using _countdown_shot_limiting_type =
    uint16_t;
  _countdown_shot_limiting_type countdown_shot_limiting;
  using _thermal_shutdown_type =
    uint8_t;
  _thermal_shutdown_type thermal_shutdown;
  using _shot_limiting_type =
    uint8_t;
  _shot_limiting_type shot_limiting;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__countdown_thermal_shutdown(
    const uint16_t & _arg)
  {
    this->countdown_thermal_shutdown = _arg;
    return *this;
  }
  Type & set__countdown_shot_limiting(
    const uint16_t & _arg)
  {
    this->countdown_shot_limiting = _arg;
    return *this;
  }
  Type & set__thermal_shutdown(
    const uint8_t & _arg)
  {
    this->thermal_shutdown = _arg;
    return *this;
  }
  Type & set__shot_limiting(
    const uint8_t & _arg)
  {
    this->shot_limiting = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint8_t THERMAL_SHUTDOWN_NORMAL =
    0u;
  static constexpr uint8_t THERMAL_SHUTDOWN_IMMINENT =
    1u;
  static constexpr uint8_t SHOT_LIMITING_NORMAL =
    0u;
  static constexpr uint8_t SHOT_LIMITING_IMMINENT =
    1u;
  static constexpr uint8_t SHOT_LIMITING_REDUCTION_0_10 =
    2u;
  static constexpr uint8_t SHOT_LIMITING_REDUCTION_10_20 =
    3u;
  static constexpr uint8_t SHOT_LIMITING_REDUCTION_20_30 =
    4u;
  static constexpr uint8_t SHOT_LIMITING_REDUCTION_30_40 =
    5u;
  static constexpr uint8_t SHOT_LIMITING_REDUCTION_40_50 =
    6u;
  static constexpr uint8_t SHOT_LIMITING_REDUCTION_50_60 =
    7u;
  static constexpr uint8_t SHOT_LIMITING_REDUCTION_60_70 =
    8u;
  static constexpr uint8_t SHOT_LIMITING_REDUCTION_70_75 =
    9u;

  // pointer types
  using RawPtr =
    ouster_sensor_msgs::msg::Telemetry_<ContainerAllocator> *;
  using ConstRawPtr =
    const ouster_sensor_msgs::msg::Telemetry_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ouster_sensor_msgs::msg::Telemetry_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ouster_sensor_msgs::msg::Telemetry_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ouster_sensor_msgs::msg::Telemetry_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ouster_sensor_msgs::msg::Telemetry_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ouster_sensor_msgs::msg::Telemetry_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ouster_sensor_msgs::msg::Telemetry_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ouster_sensor_msgs::msg::Telemetry_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ouster_sensor_msgs::msg::Telemetry_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ouster_sensor_msgs__msg__Telemetry
    std::shared_ptr<ouster_sensor_msgs::msg::Telemetry_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ouster_sensor_msgs__msg__Telemetry
    std::shared_ptr<ouster_sensor_msgs::msg::Telemetry_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Telemetry_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->countdown_thermal_shutdown != other.countdown_thermal_shutdown) {
      return false;
    }
    if (this->countdown_shot_limiting != other.countdown_shot_limiting) {
      return false;
    }
    if (this->thermal_shutdown != other.thermal_shutdown) {
      return false;
    }
    if (this->shot_limiting != other.shot_limiting) {
      return false;
    }
    return true;
  }
  bool operator!=(const Telemetry_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Telemetry_

// alias to use template instance with default allocator
using Telemetry =
  ouster_sensor_msgs::msg::Telemetry_<std::allocator<void>>;

// constant definitions
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t Telemetry_<ContainerAllocator>::THERMAL_SHUTDOWN_NORMAL;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t Telemetry_<ContainerAllocator>::THERMAL_SHUTDOWN_IMMINENT;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t Telemetry_<ContainerAllocator>::SHOT_LIMITING_NORMAL;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t Telemetry_<ContainerAllocator>::SHOT_LIMITING_IMMINENT;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t Telemetry_<ContainerAllocator>::SHOT_LIMITING_REDUCTION_0_10;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t Telemetry_<ContainerAllocator>::SHOT_LIMITING_REDUCTION_10_20;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t Telemetry_<ContainerAllocator>::SHOT_LIMITING_REDUCTION_20_30;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t Telemetry_<ContainerAllocator>::SHOT_LIMITING_REDUCTION_30_40;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t Telemetry_<ContainerAllocator>::SHOT_LIMITING_REDUCTION_40_50;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t Telemetry_<ContainerAllocator>::SHOT_LIMITING_REDUCTION_50_60;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t Telemetry_<ContainerAllocator>::SHOT_LIMITING_REDUCTION_60_70;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t Telemetry_<ContainerAllocator>::SHOT_LIMITING_REDUCTION_70_75;
#endif  // __cplusplus < 201703L

}  // namespace msg

}  // namespace ouster_sensor_msgs

#endif  // OUSTER_SENSOR_MSGS__MSG__DETAIL__TELEMETRY__STRUCT_HPP_

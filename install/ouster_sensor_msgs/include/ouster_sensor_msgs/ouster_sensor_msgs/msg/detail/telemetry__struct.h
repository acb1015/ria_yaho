// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ouster_sensor_msgs:msg/Telemetry.idl
// generated code does not contain a copyright notice

#ifndef OUSTER_SENSOR_MSGS__MSG__DETAIL__TELEMETRY__STRUCT_H_
#define OUSTER_SENSOR_MSGS__MSG__DETAIL__TELEMETRY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'THERMAL_SHUTDOWN_NORMAL'.
/**
  * ThermalShutdownStatus thermal_shutdown
  * Normal operation
 */
enum
{
  ouster_sensor_msgs__msg__Telemetry__THERMAL_SHUTDOWN_NORMAL = 0
};

/// Constant 'THERMAL_SHUTDOWN_IMMINENT'.
/**
  * Thermal Shutdown imminent
 */
enum
{
  ouster_sensor_msgs__msg__Telemetry__THERMAL_SHUTDOWN_IMMINENT = 1
};

/// Constant 'SHOT_LIMITING_NORMAL'.
/**
  * ShotLimitingStatus shot_limiting
  * Normal operation
 */
enum
{
  ouster_sensor_msgs__msg__Telemetry__SHOT_LIMITING_NORMAL = 0
};

/// Constant 'SHOT_LIMITING_IMMINENT'.
/**
  * Shot limiting imminent
 */
enum
{
  ouster_sensor_msgs__msg__Telemetry__SHOT_LIMITING_IMMINENT = 1
};

/// Constant 'SHOT_LIMITING_REDUCTION_0_10'.
/**
  * Shot limiting reduction by 0 to 10%
 */
enum
{
  ouster_sensor_msgs__msg__Telemetry__SHOT_LIMITING_REDUCTION_0_10 = 2
};

/// Constant 'SHOT_LIMITING_REDUCTION_10_20'.
/**
  * Shot limiting reduction by 10 to 20%
 */
enum
{
  ouster_sensor_msgs__msg__Telemetry__SHOT_LIMITING_REDUCTION_10_20 = 3
};

/// Constant 'SHOT_LIMITING_REDUCTION_20_30'.
/**
  * Shot limiting reduction by 20 to 30%
 */
enum
{
  ouster_sensor_msgs__msg__Telemetry__SHOT_LIMITING_REDUCTION_20_30 = 4
};

/// Constant 'SHOT_LIMITING_REDUCTION_30_40'.
/**
  * Shot limiting reduction by 30 to 40%
 */
enum
{
  ouster_sensor_msgs__msg__Telemetry__SHOT_LIMITING_REDUCTION_30_40 = 5
};

/// Constant 'SHOT_LIMITING_REDUCTION_40_50'.
/**
  * Shot limiting reduction by 40 to 50%
 */
enum
{
  ouster_sensor_msgs__msg__Telemetry__SHOT_LIMITING_REDUCTION_40_50 = 6
};

/// Constant 'SHOT_LIMITING_REDUCTION_50_60'.
/**
  * Shot limiting reduction by 50 to 60%
 */
enum
{
  ouster_sensor_msgs__msg__Telemetry__SHOT_LIMITING_REDUCTION_50_60 = 7
};

/// Constant 'SHOT_LIMITING_REDUCTION_60_70'.
/**
  * Shot limiting reduction by 60 to 70%
 */
enum
{
  ouster_sensor_msgs__msg__Telemetry__SHOT_LIMITING_REDUCTION_60_70 = 8
};

/// Constant 'SHOT_LIMITING_REDUCTION_70_75'.
/**
  * Shot limiting reduction by 70 to 80%
 */
enum
{
  ouster_sensor_msgs__msg__Telemetry__SHOT_LIMITING_REDUCTION_70_75 = 9
};

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

/// Struct defined in msg/Telemetry in the package ouster_sensor_msgs.
/**
  * This message defines the telemetry data for Ouster sensors.
 */
typedef struct ouster_sensor_msgs__msg__Telemetry
{
  /// Message header
  std_msgs__msg__Header header;
  /// Telemetry fields for more information on these fields and their meaning, please review:
  /// https://static.ouster.dev/sensor-docs/image_route1/image_route2/thermal_int_guide/therm_int_guide.html
  /// the thermal shutdown countdown.
  uint16_t countdown_thermal_shutdown;
  /// the shot limiting countdown.
  uint16_t countdown_shot_limiting;
  /// the thermal shutdown status. 0 = NORMAL, 1 = SHUTDOWN IMMINENT.
  uint8_t thermal_shutdown;
  /// the shot limiting status. 0 = NORMAL OPERATION.
  uint8_t shot_limiting;
} ouster_sensor_msgs__msg__Telemetry;

// Struct for a sequence of ouster_sensor_msgs__msg__Telemetry.
typedef struct ouster_sensor_msgs__msg__Telemetry__Sequence
{
  ouster_sensor_msgs__msg__Telemetry * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ouster_sensor_msgs__msg__Telemetry__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // OUSTER_SENSOR_MSGS__MSG__DETAIL__TELEMETRY__STRUCT_H_

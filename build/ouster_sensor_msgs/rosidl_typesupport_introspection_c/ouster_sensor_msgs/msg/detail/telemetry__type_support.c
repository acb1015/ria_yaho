// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from ouster_sensor_msgs:msg/Telemetry.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "ouster_sensor_msgs/msg/detail/telemetry__rosidl_typesupport_introspection_c.h"
#include "ouster_sensor_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "ouster_sensor_msgs/msg/detail/telemetry__functions.h"
#include "ouster_sensor_msgs/msg/detail/telemetry__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void ouster_sensor_msgs__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ouster_sensor_msgs__msg__Telemetry__init(message_memory);
}

void ouster_sensor_msgs__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_fini_function(void * message_memory)
{
  ouster_sensor_msgs__msg__Telemetry__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember ouster_sensor_msgs__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_message_member_array[5] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ouster_sensor_msgs__msg__Telemetry, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "countdown_thermal_shutdown",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ouster_sensor_msgs__msg__Telemetry, countdown_thermal_shutdown),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "countdown_shot_limiting",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ouster_sensor_msgs__msg__Telemetry, countdown_shot_limiting),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "thermal_shutdown",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ouster_sensor_msgs__msg__Telemetry, thermal_shutdown),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "shot_limiting",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ouster_sensor_msgs__msg__Telemetry, shot_limiting),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers ouster_sensor_msgs__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_message_members = {
  "ouster_sensor_msgs__msg",  // message namespace
  "Telemetry",  // message name
  5,  // number of fields
  sizeof(ouster_sensor_msgs__msg__Telemetry),
  ouster_sensor_msgs__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_message_member_array,  // message members
  ouster_sensor_msgs__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_init_function,  // function to initialize message memory (memory has to be allocated)
  ouster_sensor_msgs__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t ouster_sensor_msgs__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_message_type_support_handle = {
  0,
  &ouster_sensor_msgs__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ouster_sensor_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ouster_sensor_msgs, msg, Telemetry)() {
  ouster_sensor_msgs__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  if (!ouster_sensor_msgs__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_message_type_support_handle.typesupport_identifier) {
    ouster_sensor_msgs__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &ouster_sensor_msgs__msg__Telemetry__rosidl_typesupport_introspection_c__Telemetry_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

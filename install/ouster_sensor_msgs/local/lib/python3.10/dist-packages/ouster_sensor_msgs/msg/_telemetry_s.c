// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from ouster_sensor_msgs:msg/Telemetry.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "ouster_sensor_msgs/msg/detail/telemetry__struct.h"
#include "ouster_sensor_msgs/msg/detail/telemetry__functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool ouster_sensor_msgs__msg__telemetry__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[44];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("ouster_sensor_msgs.msg._telemetry.Telemetry", full_classname_dest, 43) == 0);
  }
  ouster_sensor_msgs__msg__Telemetry * ros_message = _ros_message;
  {  // header
    PyObject * field = PyObject_GetAttrString(_pymsg, "header");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__header__convert_from_py(field, &ros_message->header)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // countdown_thermal_shutdown
    PyObject * field = PyObject_GetAttrString(_pymsg, "countdown_thermal_shutdown");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->countdown_thermal_shutdown = (uint16_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // countdown_shot_limiting
    PyObject * field = PyObject_GetAttrString(_pymsg, "countdown_shot_limiting");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->countdown_shot_limiting = (uint16_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // thermal_shutdown
    PyObject * field = PyObject_GetAttrString(_pymsg, "thermal_shutdown");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->thermal_shutdown = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // shot_limiting
    PyObject * field = PyObject_GetAttrString(_pymsg, "shot_limiting");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->shot_limiting = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * ouster_sensor_msgs__msg__telemetry__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Telemetry */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ouster_sensor_msgs.msg._telemetry");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Telemetry");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ouster_sensor_msgs__msg__Telemetry * ros_message = (ouster_sensor_msgs__msg__Telemetry *)raw_ros_message;
  {  // header
    PyObject * field = NULL;
    field = std_msgs__msg__header__convert_to_py(&ros_message->header);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "header", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // countdown_thermal_shutdown
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->countdown_thermal_shutdown);
    {
      int rc = PyObject_SetAttrString(_pymessage, "countdown_thermal_shutdown", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // countdown_shot_limiting
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->countdown_shot_limiting);
    {
      int rc = PyObject_SetAttrString(_pymessage, "countdown_shot_limiting", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // thermal_shutdown
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->thermal_shutdown);
    {
      int rc = PyObject_SetAttrString(_pymessage, "thermal_shutdown", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // shot_limiting
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->shot_limiting);
    {
      int rc = PyObject_SetAttrString(_pymessage, "shot_limiting", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

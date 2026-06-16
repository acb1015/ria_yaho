// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ouster_sensor_msgs:msg/Telemetry.idl
// generated code does not contain a copyright notice
#include "ouster_sensor_msgs/msg/detail/telemetry__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
ouster_sensor_msgs__msg__Telemetry__init(ouster_sensor_msgs__msg__Telemetry * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    ouster_sensor_msgs__msg__Telemetry__fini(msg);
    return false;
  }
  // countdown_thermal_shutdown
  // countdown_shot_limiting
  // thermal_shutdown
  // shot_limiting
  return true;
}

void
ouster_sensor_msgs__msg__Telemetry__fini(ouster_sensor_msgs__msg__Telemetry * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // countdown_thermal_shutdown
  // countdown_shot_limiting
  // thermal_shutdown
  // shot_limiting
}

bool
ouster_sensor_msgs__msg__Telemetry__are_equal(const ouster_sensor_msgs__msg__Telemetry * lhs, const ouster_sensor_msgs__msg__Telemetry * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // countdown_thermal_shutdown
  if (lhs->countdown_thermal_shutdown != rhs->countdown_thermal_shutdown) {
    return false;
  }
  // countdown_shot_limiting
  if (lhs->countdown_shot_limiting != rhs->countdown_shot_limiting) {
    return false;
  }
  // thermal_shutdown
  if (lhs->thermal_shutdown != rhs->thermal_shutdown) {
    return false;
  }
  // shot_limiting
  if (lhs->shot_limiting != rhs->shot_limiting) {
    return false;
  }
  return true;
}

bool
ouster_sensor_msgs__msg__Telemetry__copy(
  const ouster_sensor_msgs__msg__Telemetry * input,
  ouster_sensor_msgs__msg__Telemetry * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // countdown_thermal_shutdown
  output->countdown_thermal_shutdown = input->countdown_thermal_shutdown;
  // countdown_shot_limiting
  output->countdown_shot_limiting = input->countdown_shot_limiting;
  // thermal_shutdown
  output->thermal_shutdown = input->thermal_shutdown;
  // shot_limiting
  output->shot_limiting = input->shot_limiting;
  return true;
}

ouster_sensor_msgs__msg__Telemetry *
ouster_sensor_msgs__msg__Telemetry__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ouster_sensor_msgs__msg__Telemetry * msg = (ouster_sensor_msgs__msg__Telemetry *)allocator.allocate(sizeof(ouster_sensor_msgs__msg__Telemetry), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ouster_sensor_msgs__msg__Telemetry));
  bool success = ouster_sensor_msgs__msg__Telemetry__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
ouster_sensor_msgs__msg__Telemetry__destroy(ouster_sensor_msgs__msg__Telemetry * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    ouster_sensor_msgs__msg__Telemetry__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
ouster_sensor_msgs__msg__Telemetry__Sequence__init(ouster_sensor_msgs__msg__Telemetry__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ouster_sensor_msgs__msg__Telemetry * data = NULL;

  if (size) {
    data = (ouster_sensor_msgs__msg__Telemetry *)allocator.zero_allocate(size, sizeof(ouster_sensor_msgs__msg__Telemetry), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ouster_sensor_msgs__msg__Telemetry__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ouster_sensor_msgs__msg__Telemetry__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
ouster_sensor_msgs__msg__Telemetry__Sequence__fini(ouster_sensor_msgs__msg__Telemetry__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      ouster_sensor_msgs__msg__Telemetry__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

ouster_sensor_msgs__msg__Telemetry__Sequence *
ouster_sensor_msgs__msg__Telemetry__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ouster_sensor_msgs__msg__Telemetry__Sequence * array = (ouster_sensor_msgs__msg__Telemetry__Sequence *)allocator.allocate(sizeof(ouster_sensor_msgs__msg__Telemetry__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = ouster_sensor_msgs__msg__Telemetry__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
ouster_sensor_msgs__msg__Telemetry__Sequence__destroy(ouster_sensor_msgs__msg__Telemetry__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    ouster_sensor_msgs__msg__Telemetry__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
ouster_sensor_msgs__msg__Telemetry__Sequence__are_equal(const ouster_sensor_msgs__msg__Telemetry__Sequence * lhs, const ouster_sensor_msgs__msg__Telemetry__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!ouster_sensor_msgs__msg__Telemetry__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
ouster_sensor_msgs__msg__Telemetry__Sequence__copy(
  const ouster_sensor_msgs__msg__Telemetry__Sequence * input,
  ouster_sensor_msgs__msg__Telemetry__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(ouster_sensor_msgs__msg__Telemetry);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    ouster_sensor_msgs__msg__Telemetry * data =
      (ouster_sensor_msgs__msg__Telemetry *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!ouster_sensor_msgs__msg__Telemetry__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          ouster_sensor_msgs__msg__Telemetry__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!ouster_sensor_msgs__msg__Telemetry__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}

// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from speech_to_goal_interfaces:srv/LLMQuery.idl
// generated code does not contain a copyright notice
#include "speech_to_goal_interfaces/srv/detail/llm_query__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `query`
#include "rosidl_runtime_c/string_functions.h"

bool
speech_to_goal_interfaces__srv__LLMQuery_Request__init(speech_to_goal_interfaces__srv__LLMQuery_Request * msg)
{
  if (!msg) {
    return false;
  }
  // query
  if (!rosidl_runtime_c__String__init(&msg->query)) {
    speech_to_goal_interfaces__srv__LLMQuery_Request__fini(msg);
    return false;
  }
  return true;
}

void
speech_to_goal_interfaces__srv__LLMQuery_Request__fini(speech_to_goal_interfaces__srv__LLMQuery_Request * msg)
{
  if (!msg) {
    return;
  }
  // query
  rosidl_runtime_c__String__fini(&msg->query);
}

bool
speech_to_goal_interfaces__srv__LLMQuery_Request__are_equal(const speech_to_goal_interfaces__srv__LLMQuery_Request * lhs, const speech_to_goal_interfaces__srv__LLMQuery_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // query
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->query), &(rhs->query)))
  {
    return false;
  }
  return true;
}

bool
speech_to_goal_interfaces__srv__LLMQuery_Request__copy(
  const speech_to_goal_interfaces__srv__LLMQuery_Request * input,
  speech_to_goal_interfaces__srv__LLMQuery_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // query
  if (!rosidl_runtime_c__String__copy(
      &(input->query), &(output->query)))
  {
    return false;
  }
  return true;
}

speech_to_goal_interfaces__srv__LLMQuery_Request *
speech_to_goal_interfaces__srv__LLMQuery_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  speech_to_goal_interfaces__srv__LLMQuery_Request * msg = (speech_to_goal_interfaces__srv__LLMQuery_Request *)allocator.allocate(sizeof(speech_to_goal_interfaces__srv__LLMQuery_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(speech_to_goal_interfaces__srv__LLMQuery_Request));
  bool success = speech_to_goal_interfaces__srv__LLMQuery_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
speech_to_goal_interfaces__srv__LLMQuery_Request__destroy(speech_to_goal_interfaces__srv__LLMQuery_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    speech_to_goal_interfaces__srv__LLMQuery_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence__init(speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  speech_to_goal_interfaces__srv__LLMQuery_Request * data = NULL;

  if (size) {
    data = (speech_to_goal_interfaces__srv__LLMQuery_Request *)allocator.zero_allocate(size, sizeof(speech_to_goal_interfaces__srv__LLMQuery_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = speech_to_goal_interfaces__srv__LLMQuery_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        speech_to_goal_interfaces__srv__LLMQuery_Request__fini(&data[i - 1]);
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
speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence__fini(speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence * array)
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
      speech_to_goal_interfaces__srv__LLMQuery_Request__fini(&array->data[i]);
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

speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence *
speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence * array = (speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence *)allocator.allocate(sizeof(speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence__destroy(speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence__are_equal(const speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence * lhs, const speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!speech_to_goal_interfaces__srv__LLMQuery_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence__copy(
  const speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence * input,
  speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(speech_to_goal_interfaces__srv__LLMQuery_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    speech_to_goal_interfaces__srv__LLMQuery_Request * data =
      (speech_to_goal_interfaces__srv__LLMQuery_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!speech_to_goal_interfaces__srv__LLMQuery_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          speech_to_goal_interfaces__srv__LLMQuery_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!speech_to_goal_interfaces__srv__LLMQuery_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `waypoints`
#include "speech_to_goal_interfaces/msg/detail/waypoint__functions.h"
// Member `message`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

bool
speech_to_goal_interfaces__srv__LLMQuery_Response__init(speech_to_goal_interfaces__srv__LLMQuery_Response * msg)
{
  if (!msg) {
    return false;
  }
  // waypoints
  if (!speech_to_goal_interfaces__msg__Waypoint__Sequence__init(&msg->waypoints, 0)) {
    speech_to_goal_interfaces__srv__LLMQuery_Response__fini(msg);
    return false;
  }
  // success
  // message
  if (!rosidl_runtime_c__String__init(&msg->message)) {
    speech_to_goal_interfaces__srv__LLMQuery_Response__fini(msg);
    return false;
  }
  return true;
}

void
speech_to_goal_interfaces__srv__LLMQuery_Response__fini(speech_to_goal_interfaces__srv__LLMQuery_Response * msg)
{
  if (!msg) {
    return;
  }
  // waypoints
  speech_to_goal_interfaces__msg__Waypoint__Sequence__fini(&msg->waypoints);
  // success
  // message
  rosidl_runtime_c__String__fini(&msg->message);
}

bool
speech_to_goal_interfaces__srv__LLMQuery_Response__are_equal(const speech_to_goal_interfaces__srv__LLMQuery_Response * lhs, const speech_to_goal_interfaces__srv__LLMQuery_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // waypoints
  if (!speech_to_goal_interfaces__msg__Waypoint__Sequence__are_equal(
      &(lhs->waypoints), &(rhs->waypoints)))
  {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  // message
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->message), &(rhs->message)))
  {
    return false;
  }
  return true;
}

bool
speech_to_goal_interfaces__srv__LLMQuery_Response__copy(
  const speech_to_goal_interfaces__srv__LLMQuery_Response * input,
  speech_to_goal_interfaces__srv__LLMQuery_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // waypoints
  if (!speech_to_goal_interfaces__msg__Waypoint__Sequence__copy(
      &(input->waypoints), &(output->waypoints)))
  {
    return false;
  }
  // success
  output->success = input->success;
  // message
  if (!rosidl_runtime_c__String__copy(
      &(input->message), &(output->message)))
  {
    return false;
  }
  return true;
}

speech_to_goal_interfaces__srv__LLMQuery_Response *
speech_to_goal_interfaces__srv__LLMQuery_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  speech_to_goal_interfaces__srv__LLMQuery_Response * msg = (speech_to_goal_interfaces__srv__LLMQuery_Response *)allocator.allocate(sizeof(speech_to_goal_interfaces__srv__LLMQuery_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(speech_to_goal_interfaces__srv__LLMQuery_Response));
  bool success = speech_to_goal_interfaces__srv__LLMQuery_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
speech_to_goal_interfaces__srv__LLMQuery_Response__destroy(speech_to_goal_interfaces__srv__LLMQuery_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    speech_to_goal_interfaces__srv__LLMQuery_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence__init(speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  speech_to_goal_interfaces__srv__LLMQuery_Response * data = NULL;

  if (size) {
    data = (speech_to_goal_interfaces__srv__LLMQuery_Response *)allocator.zero_allocate(size, sizeof(speech_to_goal_interfaces__srv__LLMQuery_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = speech_to_goal_interfaces__srv__LLMQuery_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        speech_to_goal_interfaces__srv__LLMQuery_Response__fini(&data[i - 1]);
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
speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence__fini(speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence * array)
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
      speech_to_goal_interfaces__srv__LLMQuery_Response__fini(&array->data[i]);
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

speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence *
speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence * array = (speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence *)allocator.allocate(sizeof(speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence__destroy(speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence__are_equal(const speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence * lhs, const speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!speech_to_goal_interfaces__srv__LLMQuery_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence__copy(
  const speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence * input,
  speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(speech_to_goal_interfaces__srv__LLMQuery_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    speech_to_goal_interfaces__srv__LLMQuery_Response * data =
      (speech_to_goal_interfaces__srv__LLMQuery_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!speech_to_goal_interfaces__srv__LLMQuery_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          speech_to_goal_interfaces__srv__LLMQuery_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!speech_to_goal_interfaces__srv__LLMQuery_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}

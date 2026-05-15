// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from object_recognition_interfaces:srv/DetectObject.idl
// generated code does not contain a copyright notice
#include "object_recognition_interfaces/srv/detail/detect_object__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
object_recognition_interfaces__srv__DetectObject_Request__init(object_recognition_interfaces__srv__DetectObject_Request * msg)
{
  if (!msg) {
    return false;
  }
  // structure_needs_at_least_one_member
  return true;
}

void
object_recognition_interfaces__srv__DetectObject_Request__fini(object_recognition_interfaces__srv__DetectObject_Request * msg)
{
  if (!msg) {
    return;
  }
  // structure_needs_at_least_one_member
}

bool
object_recognition_interfaces__srv__DetectObject_Request__are_equal(const object_recognition_interfaces__srv__DetectObject_Request * lhs, const object_recognition_interfaces__srv__DetectObject_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // structure_needs_at_least_one_member
  if (lhs->structure_needs_at_least_one_member != rhs->structure_needs_at_least_one_member) {
    return false;
  }
  return true;
}

bool
object_recognition_interfaces__srv__DetectObject_Request__copy(
  const object_recognition_interfaces__srv__DetectObject_Request * input,
  object_recognition_interfaces__srv__DetectObject_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // structure_needs_at_least_one_member
  output->structure_needs_at_least_one_member = input->structure_needs_at_least_one_member;
  return true;
}

object_recognition_interfaces__srv__DetectObject_Request *
object_recognition_interfaces__srv__DetectObject_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  object_recognition_interfaces__srv__DetectObject_Request * msg = (object_recognition_interfaces__srv__DetectObject_Request *)allocator.allocate(sizeof(object_recognition_interfaces__srv__DetectObject_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(object_recognition_interfaces__srv__DetectObject_Request));
  bool success = object_recognition_interfaces__srv__DetectObject_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
object_recognition_interfaces__srv__DetectObject_Request__destroy(object_recognition_interfaces__srv__DetectObject_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    object_recognition_interfaces__srv__DetectObject_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
object_recognition_interfaces__srv__DetectObject_Request__Sequence__init(object_recognition_interfaces__srv__DetectObject_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  object_recognition_interfaces__srv__DetectObject_Request * data = NULL;

  if (size) {
    data = (object_recognition_interfaces__srv__DetectObject_Request *)allocator.zero_allocate(size, sizeof(object_recognition_interfaces__srv__DetectObject_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = object_recognition_interfaces__srv__DetectObject_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        object_recognition_interfaces__srv__DetectObject_Request__fini(&data[i - 1]);
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
object_recognition_interfaces__srv__DetectObject_Request__Sequence__fini(object_recognition_interfaces__srv__DetectObject_Request__Sequence * array)
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
      object_recognition_interfaces__srv__DetectObject_Request__fini(&array->data[i]);
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

object_recognition_interfaces__srv__DetectObject_Request__Sequence *
object_recognition_interfaces__srv__DetectObject_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  object_recognition_interfaces__srv__DetectObject_Request__Sequence * array = (object_recognition_interfaces__srv__DetectObject_Request__Sequence *)allocator.allocate(sizeof(object_recognition_interfaces__srv__DetectObject_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = object_recognition_interfaces__srv__DetectObject_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
object_recognition_interfaces__srv__DetectObject_Request__Sequence__destroy(object_recognition_interfaces__srv__DetectObject_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    object_recognition_interfaces__srv__DetectObject_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
object_recognition_interfaces__srv__DetectObject_Request__Sequence__are_equal(const object_recognition_interfaces__srv__DetectObject_Request__Sequence * lhs, const object_recognition_interfaces__srv__DetectObject_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!object_recognition_interfaces__srv__DetectObject_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
object_recognition_interfaces__srv__DetectObject_Request__Sequence__copy(
  const object_recognition_interfaces__srv__DetectObject_Request__Sequence * input,
  object_recognition_interfaces__srv__DetectObject_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(object_recognition_interfaces__srv__DetectObject_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    object_recognition_interfaces__srv__DetectObject_Request * data =
      (object_recognition_interfaces__srv__DetectObject_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!object_recognition_interfaces__srv__DetectObject_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          object_recognition_interfaces__srv__DetectObject_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!object_recognition_interfaces__srv__DetectObject_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `object`
#include "rosidl_runtime_c/string_functions.h"

bool
object_recognition_interfaces__srv__DetectObject_Response__init(object_recognition_interfaces__srv__DetectObject_Response * msg)
{
  if (!msg) {
    return false;
  }
  // object
  if (!rosidl_runtime_c__String__init(&msg->object)) {
    object_recognition_interfaces__srv__DetectObject_Response__fini(msg);
    return false;
  }
  // confidence
  // success
  return true;
}

void
object_recognition_interfaces__srv__DetectObject_Response__fini(object_recognition_interfaces__srv__DetectObject_Response * msg)
{
  if (!msg) {
    return;
  }
  // object
  rosidl_runtime_c__String__fini(&msg->object);
  // confidence
  // success
}

bool
object_recognition_interfaces__srv__DetectObject_Response__are_equal(const object_recognition_interfaces__srv__DetectObject_Response * lhs, const object_recognition_interfaces__srv__DetectObject_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // object
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->object), &(rhs->object)))
  {
    return false;
  }
  // confidence
  if (lhs->confidence != rhs->confidence) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  return true;
}

bool
object_recognition_interfaces__srv__DetectObject_Response__copy(
  const object_recognition_interfaces__srv__DetectObject_Response * input,
  object_recognition_interfaces__srv__DetectObject_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // object
  if (!rosidl_runtime_c__String__copy(
      &(input->object), &(output->object)))
  {
    return false;
  }
  // confidence
  output->confidence = input->confidence;
  // success
  output->success = input->success;
  return true;
}

object_recognition_interfaces__srv__DetectObject_Response *
object_recognition_interfaces__srv__DetectObject_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  object_recognition_interfaces__srv__DetectObject_Response * msg = (object_recognition_interfaces__srv__DetectObject_Response *)allocator.allocate(sizeof(object_recognition_interfaces__srv__DetectObject_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(object_recognition_interfaces__srv__DetectObject_Response));
  bool success = object_recognition_interfaces__srv__DetectObject_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
object_recognition_interfaces__srv__DetectObject_Response__destroy(object_recognition_interfaces__srv__DetectObject_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    object_recognition_interfaces__srv__DetectObject_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
object_recognition_interfaces__srv__DetectObject_Response__Sequence__init(object_recognition_interfaces__srv__DetectObject_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  object_recognition_interfaces__srv__DetectObject_Response * data = NULL;

  if (size) {
    data = (object_recognition_interfaces__srv__DetectObject_Response *)allocator.zero_allocate(size, sizeof(object_recognition_interfaces__srv__DetectObject_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = object_recognition_interfaces__srv__DetectObject_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        object_recognition_interfaces__srv__DetectObject_Response__fini(&data[i - 1]);
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
object_recognition_interfaces__srv__DetectObject_Response__Sequence__fini(object_recognition_interfaces__srv__DetectObject_Response__Sequence * array)
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
      object_recognition_interfaces__srv__DetectObject_Response__fini(&array->data[i]);
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

object_recognition_interfaces__srv__DetectObject_Response__Sequence *
object_recognition_interfaces__srv__DetectObject_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  object_recognition_interfaces__srv__DetectObject_Response__Sequence * array = (object_recognition_interfaces__srv__DetectObject_Response__Sequence *)allocator.allocate(sizeof(object_recognition_interfaces__srv__DetectObject_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = object_recognition_interfaces__srv__DetectObject_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
object_recognition_interfaces__srv__DetectObject_Response__Sequence__destroy(object_recognition_interfaces__srv__DetectObject_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    object_recognition_interfaces__srv__DetectObject_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
object_recognition_interfaces__srv__DetectObject_Response__Sequence__are_equal(const object_recognition_interfaces__srv__DetectObject_Response__Sequence * lhs, const object_recognition_interfaces__srv__DetectObject_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!object_recognition_interfaces__srv__DetectObject_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
object_recognition_interfaces__srv__DetectObject_Response__Sequence__copy(
  const object_recognition_interfaces__srv__DetectObject_Response__Sequence * input,
  object_recognition_interfaces__srv__DetectObject_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(object_recognition_interfaces__srv__DetectObject_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    object_recognition_interfaces__srv__DetectObject_Response * data =
      (object_recognition_interfaces__srv__DetectObject_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!object_recognition_interfaces__srv__DetectObject_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          object_recognition_interfaces__srv__DetectObject_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!object_recognition_interfaces__srv__DetectObject_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}

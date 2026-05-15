// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from object_recognition_interfaces:srv/AddObject.idl
// generated code does not contain a copyright notice
#include "object_recognition_interfaces/srv/detail/add_object__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `name`
#include "rosidl_runtime_c/string_functions.h"

bool
object_recognition_interfaces__srv__AddObject_Request__init(object_recognition_interfaces__srv__AddObject_Request * msg)
{
  if (!msg) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__init(&msg->name)) {
    object_recognition_interfaces__srv__AddObject_Request__fini(msg);
    return false;
  }
  // x
  // y
  // z
  return true;
}

void
object_recognition_interfaces__srv__AddObject_Request__fini(object_recognition_interfaces__srv__AddObject_Request * msg)
{
  if (!msg) {
    return;
  }
  // name
  rosidl_runtime_c__String__fini(&msg->name);
  // x
  // y
  // z
}

bool
object_recognition_interfaces__srv__AddObject_Request__are_equal(const object_recognition_interfaces__srv__AddObject_Request * lhs, const object_recognition_interfaces__srv__AddObject_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->name), &(rhs->name)))
  {
    return false;
  }
  // x
  if (lhs->x != rhs->x) {
    return false;
  }
  // y
  if (lhs->y != rhs->y) {
    return false;
  }
  // z
  if (lhs->z != rhs->z) {
    return false;
  }
  return true;
}

bool
object_recognition_interfaces__srv__AddObject_Request__copy(
  const object_recognition_interfaces__srv__AddObject_Request * input,
  object_recognition_interfaces__srv__AddObject_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__copy(
      &(input->name), &(output->name)))
  {
    return false;
  }
  // x
  output->x = input->x;
  // y
  output->y = input->y;
  // z
  output->z = input->z;
  return true;
}

object_recognition_interfaces__srv__AddObject_Request *
object_recognition_interfaces__srv__AddObject_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  object_recognition_interfaces__srv__AddObject_Request * msg = (object_recognition_interfaces__srv__AddObject_Request *)allocator.allocate(sizeof(object_recognition_interfaces__srv__AddObject_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(object_recognition_interfaces__srv__AddObject_Request));
  bool success = object_recognition_interfaces__srv__AddObject_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
object_recognition_interfaces__srv__AddObject_Request__destroy(object_recognition_interfaces__srv__AddObject_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    object_recognition_interfaces__srv__AddObject_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
object_recognition_interfaces__srv__AddObject_Request__Sequence__init(object_recognition_interfaces__srv__AddObject_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  object_recognition_interfaces__srv__AddObject_Request * data = NULL;

  if (size) {
    data = (object_recognition_interfaces__srv__AddObject_Request *)allocator.zero_allocate(size, sizeof(object_recognition_interfaces__srv__AddObject_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = object_recognition_interfaces__srv__AddObject_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        object_recognition_interfaces__srv__AddObject_Request__fini(&data[i - 1]);
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
object_recognition_interfaces__srv__AddObject_Request__Sequence__fini(object_recognition_interfaces__srv__AddObject_Request__Sequence * array)
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
      object_recognition_interfaces__srv__AddObject_Request__fini(&array->data[i]);
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

object_recognition_interfaces__srv__AddObject_Request__Sequence *
object_recognition_interfaces__srv__AddObject_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  object_recognition_interfaces__srv__AddObject_Request__Sequence * array = (object_recognition_interfaces__srv__AddObject_Request__Sequence *)allocator.allocate(sizeof(object_recognition_interfaces__srv__AddObject_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = object_recognition_interfaces__srv__AddObject_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
object_recognition_interfaces__srv__AddObject_Request__Sequence__destroy(object_recognition_interfaces__srv__AddObject_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    object_recognition_interfaces__srv__AddObject_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
object_recognition_interfaces__srv__AddObject_Request__Sequence__are_equal(const object_recognition_interfaces__srv__AddObject_Request__Sequence * lhs, const object_recognition_interfaces__srv__AddObject_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!object_recognition_interfaces__srv__AddObject_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
object_recognition_interfaces__srv__AddObject_Request__Sequence__copy(
  const object_recognition_interfaces__srv__AddObject_Request__Sequence * input,
  object_recognition_interfaces__srv__AddObject_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(object_recognition_interfaces__srv__AddObject_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    object_recognition_interfaces__srv__AddObject_Request * data =
      (object_recognition_interfaces__srv__AddObject_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!object_recognition_interfaces__srv__AddObject_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          object_recognition_interfaces__srv__AddObject_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!object_recognition_interfaces__srv__AddObject_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `message`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

bool
object_recognition_interfaces__srv__AddObject_Response__init(object_recognition_interfaces__srv__AddObject_Response * msg)
{
  if (!msg) {
    return false;
  }
  // success
  // message
  if (!rosidl_runtime_c__String__init(&msg->message)) {
    object_recognition_interfaces__srv__AddObject_Response__fini(msg);
    return false;
  }
  return true;
}

void
object_recognition_interfaces__srv__AddObject_Response__fini(object_recognition_interfaces__srv__AddObject_Response * msg)
{
  if (!msg) {
    return;
  }
  // success
  // message
  rosidl_runtime_c__String__fini(&msg->message);
}

bool
object_recognition_interfaces__srv__AddObject_Response__are_equal(const object_recognition_interfaces__srv__AddObject_Response * lhs, const object_recognition_interfaces__srv__AddObject_Response * rhs)
{
  if (!lhs || !rhs) {
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
object_recognition_interfaces__srv__AddObject_Response__copy(
  const object_recognition_interfaces__srv__AddObject_Response * input,
  object_recognition_interfaces__srv__AddObject_Response * output)
{
  if (!input || !output) {
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

object_recognition_interfaces__srv__AddObject_Response *
object_recognition_interfaces__srv__AddObject_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  object_recognition_interfaces__srv__AddObject_Response * msg = (object_recognition_interfaces__srv__AddObject_Response *)allocator.allocate(sizeof(object_recognition_interfaces__srv__AddObject_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(object_recognition_interfaces__srv__AddObject_Response));
  bool success = object_recognition_interfaces__srv__AddObject_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
object_recognition_interfaces__srv__AddObject_Response__destroy(object_recognition_interfaces__srv__AddObject_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    object_recognition_interfaces__srv__AddObject_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
object_recognition_interfaces__srv__AddObject_Response__Sequence__init(object_recognition_interfaces__srv__AddObject_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  object_recognition_interfaces__srv__AddObject_Response * data = NULL;

  if (size) {
    data = (object_recognition_interfaces__srv__AddObject_Response *)allocator.zero_allocate(size, sizeof(object_recognition_interfaces__srv__AddObject_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = object_recognition_interfaces__srv__AddObject_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        object_recognition_interfaces__srv__AddObject_Response__fini(&data[i - 1]);
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
object_recognition_interfaces__srv__AddObject_Response__Sequence__fini(object_recognition_interfaces__srv__AddObject_Response__Sequence * array)
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
      object_recognition_interfaces__srv__AddObject_Response__fini(&array->data[i]);
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

object_recognition_interfaces__srv__AddObject_Response__Sequence *
object_recognition_interfaces__srv__AddObject_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  object_recognition_interfaces__srv__AddObject_Response__Sequence * array = (object_recognition_interfaces__srv__AddObject_Response__Sequence *)allocator.allocate(sizeof(object_recognition_interfaces__srv__AddObject_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = object_recognition_interfaces__srv__AddObject_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
object_recognition_interfaces__srv__AddObject_Response__Sequence__destroy(object_recognition_interfaces__srv__AddObject_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    object_recognition_interfaces__srv__AddObject_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
object_recognition_interfaces__srv__AddObject_Response__Sequence__are_equal(const object_recognition_interfaces__srv__AddObject_Response__Sequence * lhs, const object_recognition_interfaces__srv__AddObject_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!object_recognition_interfaces__srv__AddObject_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
object_recognition_interfaces__srv__AddObject_Response__Sequence__copy(
  const object_recognition_interfaces__srv__AddObject_Response__Sequence * input,
  object_recognition_interfaces__srv__AddObject_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(object_recognition_interfaces__srv__AddObject_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    object_recognition_interfaces__srv__AddObject_Response * data =
      (object_recognition_interfaces__srv__AddObject_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!object_recognition_interfaces__srv__AddObject_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          object_recognition_interfaces__srv__AddObject_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!object_recognition_interfaces__srv__AddObject_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}

// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from object_recognition_interfaces:srv/AddObject.idl
// generated code does not contain a copyright notice

#ifndef OBJECT_RECOGNITION_INTERFACES__SRV__DETAIL__ADD_OBJECT__STRUCT_H_
#define OBJECT_RECOGNITION_INTERFACES__SRV__DETAIL__ADD_OBJECT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'name'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/AddObject in the package object_recognition_interfaces.
typedef struct object_recognition_interfaces__srv__AddObject_Request
{
  rosidl_runtime_c__String name;
  double x;
  double y;
  double z;
} object_recognition_interfaces__srv__AddObject_Request;

// Struct for a sequence of object_recognition_interfaces__srv__AddObject_Request.
typedef struct object_recognition_interfaces__srv__AddObject_Request__Sequence
{
  object_recognition_interfaces__srv__AddObject_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} object_recognition_interfaces__srv__AddObject_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'message'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in srv/AddObject in the package object_recognition_interfaces.
typedef struct object_recognition_interfaces__srv__AddObject_Response
{
  bool success;
  rosidl_runtime_c__String message;
} object_recognition_interfaces__srv__AddObject_Response;

// Struct for a sequence of object_recognition_interfaces__srv__AddObject_Response.
typedef struct object_recognition_interfaces__srv__AddObject_Response__Sequence
{
  object_recognition_interfaces__srv__AddObject_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} object_recognition_interfaces__srv__AddObject_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // OBJECT_RECOGNITION_INTERFACES__SRV__DETAIL__ADD_OBJECT__STRUCT_H_

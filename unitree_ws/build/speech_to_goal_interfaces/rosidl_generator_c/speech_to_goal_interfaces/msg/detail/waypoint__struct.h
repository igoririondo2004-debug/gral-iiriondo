// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from speech_to_goal_interfaces:msg/Waypoint.idl
// generated code does not contain a copyright notice

#ifndef SPEECH_TO_GOAL_INTERFACES__MSG__DETAIL__WAYPOINT__STRUCT_H_
#define SPEECH_TO_GOAL_INTERFACES__MSG__DETAIL__WAYPOINT__STRUCT_H_

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

/// Struct defined in msg/Waypoint in the package speech_to_goal_interfaces.
typedef struct speech_to_goal_interfaces__msg__Waypoint
{
  rosidl_runtime_c__String name;
  double x;
  double y;
  double z;
} speech_to_goal_interfaces__msg__Waypoint;

// Struct for a sequence of speech_to_goal_interfaces__msg__Waypoint.
typedef struct speech_to_goal_interfaces__msg__Waypoint__Sequence
{
  speech_to_goal_interfaces__msg__Waypoint * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} speech_to_goal_interfaces__msg__Waypoint__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SPEECH_TO_GOAL_INTERFACES__MSG__DETAIL__WAYPOINT__STRUCT_H_

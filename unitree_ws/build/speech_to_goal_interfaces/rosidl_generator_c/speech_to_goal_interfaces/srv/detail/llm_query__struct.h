// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from speech_to_goal_interfaces:srv/LLMQuery.idl
// generated code does not contain a copyright notice

#ifndef SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__LLM_QUERY__STRUCT_H_
#define SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__LLM_QUERY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'query'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/LLMQuery in the package speech_to_goal_interfaces.
typedef struct speech_to_goal_interfaces__srv__LLMQuery_Request
{
  rosidl_runtime_c__String query;
} speech_to_goal_interfaces__srv__LLMQuery_Request;

// Struct for a sequence of speech_to_goal_interfaces__srv__LLMQuery_Request.
typedef struct speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence
{
  speech_to_goal_interfaces__srv__LLMQuery_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'waypoints'
#include "speech_to_goal_interfaces/msg/detail/waypoint__struct.h"
// Member 'message'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in srv/LLMQuery in the package speech_to_goal_interfaces.
typedef struct speech_to_goal_interfaces__srv__LLMQuery_Response
{
  speech_to_goal_interfaces__msg__Waypoint__Sequence waypoints;
  bool success;
  rosidl_runtime_c__String message;
} speech_to_goal_interfaces__srv__LLMQuery_Response;

// Struct for a sequence of speech_to_goal_interfaces__srv__LLMQuery_Response.
typedef struct speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence
{
  speech_to_goal_interfaces__srv__LLMQuery_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__LLM_QUERY__STRUCT_H_

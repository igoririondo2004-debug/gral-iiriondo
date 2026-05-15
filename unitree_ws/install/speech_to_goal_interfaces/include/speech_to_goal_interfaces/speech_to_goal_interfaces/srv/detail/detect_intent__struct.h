// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from speech_to_goal_interfaces:srv/DetectIntent.idl
// generated code does not contain a copyright notice

#ifndef SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__DETECT_INTENT__STRUCT_H_
#define SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__DETECT_INTENT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'text'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/DetectIntent in the package speech_to_goal_interfaces.
typedef struct speech_to_goal_interfaces__srv__DetectIntent_Request
{
  rosidl_runtime_c__String text;
} speech_to_goal_interfaces__srv__DetectIntent_Request;

// Struct for a sequence of speech_to_goal_interfaces__srv__DetectIntent_Request.
typedef struct speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence
{
  speech_to_goal_interfaces__srv__DetectIntent_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'intent'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in srv/DetectIntent in the package speech_to_goal_interfaces.
typedef struct speech_to_goal_interfaces__srv__DetectIntent_Response
{
  rosidl_runtime_c__String intent;
} speech_to_goal_interfaces__srv__DetectIntent_Response;

// Struct for a sequence of speech_to_goal_interfaces__srv__DetectIntent_Response.
typedef struct speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence
{
  speech_to_goal_interfaces__srv__DetectIntent_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__DETECT_INTENT__STRUCT_H_

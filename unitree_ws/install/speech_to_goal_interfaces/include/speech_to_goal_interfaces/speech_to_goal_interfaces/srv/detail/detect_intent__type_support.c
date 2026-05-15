// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from speech_to_goal_interfaces:srv/DetectIntent.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "speech_to_goal_interfaces/srv/detail/detect_intent__rosidl_typesupport_introspection_c.h"
#include "speech_to_goal_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "speech_to_goal_interfaces/srv/detail/detect_intent__functions.h"
#include "speech_to_goal_interfaces/srv/detail/detect_intent__struct.h"


// Include directives for member types
// Member `text`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void speech_to_goal_interfaces__srv__DetectIntent_Request__rosidl_typesupport_introspection_c__DetectIntent_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  speech_to_goal_interfaces__srv__DetectIntent_Request__init(message_memory);
}

void speech_to_goal_interfaces__srv__DetectIntent_Request__rosidl_typesupport_introspection_c__DetectIntent_Request_fini_function(void * message_memory)
{
  speech_to_goal_interfaces__srv__DetectIntent_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember speech_to_goal_interfaces__srv__DetectIntent_Request__rosidl_typesupport_introspection_c__DetectIntent_Request_message_member_array[1] = {
  {
    "text",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(speech_to_goal_interfaces__srv__DetectIntent_Request, text),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers speech_to_goal_interfaces__srv__DetectIntent_Request__rosidl_typesupport_introspection_c__DetectIntent_Request_message_members = {
  "speech_to_goal_interfaces__srv",  // message namespace
  "DetectIntent_Request",  // message name
  1,  // number of fields
  sizeof(speech_to_goal_interfaces__srv__DetectIntent_Request),
  speech_to_goal_interfaces__srv__DetectIntent_Request__rosidl_typesupport_introspection_c__DetectIntent_Request_message_member_array,  // message members
  speech_to_goal_interfaces__srv__DetectIntent_Request__rosidl_typesupport_introspection_c__DetectIntent_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  speech_to_goal_interfaces__srv__DetectIntent_Request__rosidl_typesupport_introspection_c__DetectIntent_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t speech_to_goal_interfaces__srv__DetectIntent_Request__rosidl_typesupport_introspection_c__DetectIntent_Request_message_type_support_handle = {
  0,
  &speech_to_goal_interfaces__srv__DetectIntent_Request__rosidl_typesupport_introspection_c__DetectIntent_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_speech_to_goal_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, speech_to_goal_interfaces, srv, DetectIntent_Request)() {
  if (!speech_to_goal_interfaces__srv__DetectIntent_Request__rosidl_typesupport_introspection_c__DetectIntent_Request_message_type_support_handle.typesupport_identifier) {
    speech_to_goal_interfaces__srv__DetectIntent_Request__rosidl_typesupport_introspection_c__DetectIntent_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &speech_to_goal_interfaces__srv__DetectIntent_Request__rosidl_typesupport_introspection_c__DetectIntent_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "speech_to_goal_interfaces/srv/detail/detect_intent__rosidl_typesupport_introspection_c.h"
// already included above
// #include "speech_to_goal_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "speech_to_goal_interfaces/srv/detail/detect_intent__functions.h"
// already included above
// #include "speech_to_goal_interfaces/srv/detail/detect_intent__struct.h"


// Include directives for member types
// Member `intent`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void speech_to_goal_interfaces__srv__DetectIntent_Response__rosidl_typesupport_introspection_c__DetectIntent_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  speech_to_goal_interfaces__srv__DetectIntent_Response__init(message_memory);
}

void speech_to_goal_interfaces__srv__DetectIntent_Response__rosidl_typesupport_introspection_c__DetectIntent_Response_fini_function(void * message_memory)
{
  speech_to_goal_interfaces__srv__DetectIntent_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember speech_to_goal_interfaces__srv__DetectIntent_Response__rosidl_typesupport_introspection_c__DetectIntent_Response_message_member_array[1] = {
  {
    "intent",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(speech_to_goal_interfaces__srv__DetectIntent_Response, intent),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers speech_to_goal_interfaces__srv__DetectIntent_Response__rosidl_typesupport_introspection_c__DetectIntent_Response_message_members = {
  "speech_to_goal_interfaces__srv",  // message namespace
  "DetectIntent_Response",  // message name
  1,  // number of fields
  sizeof(speech_to_goal_interfaces__srv__DetectIntent_Response),
  speech_to_goal_interfaces__srv__DetectIntent_Response__rosidl_typesupport_introspection_c__DetectIntent_Response_message_member_array,  // message members
  speech_to_goal_interfaces__srv__DetectIntent_Response__rosidl_typesupport_introspection_c__DetectIntent_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  speech_to_goal_interfaces__srv__DetectIntent_Response__rosidl_typesupport_introspection_c__DetectIntent_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t speech_to_goal_interfaces__srv__DetectIntent_Response__rosidl_typesupport_introspection_c__DetectIntent_Response_message_type_support_handle = {
  0,
  &speech_to_goal_interfaces__srv__DetectIntent_Response__rosidl_typesupport_introspection_c__DetectIntent_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_speech_to_goal_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, speech_to_goal_interfaces, srv, DetectIntent_Response)() {
  if (!speech_to_goal_interfaces__srv__DetectIntent_Response__rosidl_typesupport_introspection_c__DetectIntent_Response_message_type_support_handle.typesupport_identifier) {
    speech_to_goal_interfaces__srv__DetectIntent_Response__rosidl_typesupport_introspection_c__DetectIntent_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &speech_to_goal_interfaces__srv__DetectIntent_Response__rosidl_typesupport_introspection_c__DetectIntent_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "speech_to_goal_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "speech_to_goal_interfaces/srv/detail/detect_intent__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers speech_to_goal_interfaces__srv__detail__detect_intent__rosidl_typesupport_introspection_c__DetectIntent_service_members = {
  "speech_to_goal_interfaces__srv",  // service namespace
  "DetectIntent",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // speech_to_goal_interfaces__srv__detail__detect_intent__rosidl_typesupport_introspection_c__DetectIntent_Request_message_type_support_handle,
  NULL  // response message
  // speech_to_goal_interfaces__srv__detail__detect_intent__rosidl_typesupport_introspection_c__DetectIntent_Response_message_type_support_handle
};

static rosidl_service_type_support_t speech_to_goal_interfaces__srv__detail__detect_intent__rosidl_typesupport_introspection_c__DetectIntent_service_type_support_handle = {
  0,
  &speech_to_goal_interfaces__srv__detail__detect_intent__rosidl_typesupport_introspection_c__DetectIntent_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, speech_to_goal_interfaces, srv, DetectIntent_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, speech_to_goal_interfaces, srv, DetectIntent_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_speech_to_goal_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, speech_to_goal_interfaces, srv, DetectIntent)() {
  if (!speech_to_goal_interfaces__srv__detail__detect_intent__rosidl_typesupport_introspection_c__DetectIntent_service_type_support_handle.typesupport_identifier) {
    speech_to_goal_interfaces__srv__detail__detect_intent__rosidl_typesupport_introspection_c__DetectIntent_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)speech_to_goal_interfaces__srv__detail__detect_intent__rosidl_typesupport_introspection_c__DetectIntent_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, speech_to_goal_interfaces, srv, DetectIntent_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, speech_to_goal_interfaces, srv, DetectIntent_Response)()->data;
  }

  return &speech_to_goal_interfaces__srv__detail__detect_intent__rosidl_typesupport_introspection_c__DetectIntent_service_type_support_handle;
}

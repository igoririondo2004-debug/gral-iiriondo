// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from object_recognition_interfaces:srv/AddObject.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "object_recognition_interfaces/srv/detail/add_object__rosidl_typesupport_introspection_c.h"
#include "object_recognition_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "object_recognition_interfaces/srv/detail/add_object__functions.h"
#include "object_recognition_interfaces/srv/detail/add_object__struct.h"


// Include directives for member types
// Member `name`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void object_recognition_interfaces__srv__AddObject_Request__rosidl_typesupport_introspection_c__AddObject_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  object_recognition_interfaces__srv__AddObject_Request__init(message_memory);
}

void object_recognition_interfaces__srv__AddObject_Request__rosidl_typesupport_introspection_c__AddObject_Request_fini_function(void * message_memory)
{
  object_recognition_interfaces__srv__AddObject_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember object_recognition_interfaces__srv__AddObject_Request__rosidl_typesupport_introspection_c__AddObject_Request_message_member_array[4] = {
  {
    "name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(object_recognition_interfaces__srv__AddObject_Request, name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "x",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(object_recognition_interfaces__srv__AddObject_Request, x),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "y",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(object_recognition_interfaces__srv__AddObject_Request, y),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "z",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(object_recognition_interfaces__srv__AddObject_Request, z),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers object_recognition_interfaces__srv__AddObject_Request__rosidl_typesupport_introspection_c__AddObject_Request_message_members = {
  "object_recognition_interfaces__srv",  // message namespace
  "AddObject_Request",  // message name
  4,  // number of fields
  sizeof(object_recognition_interfaces__srv__AddObject_Request),
  object_recognition_interfaces__srv__AddObject_Request__rosidl_typesupport_introspection_c__AddObject_Request_message_member_array,  // message members
  object_recognition_interfaces__srv__AddObject_Request__rosidl_typesupport_introspection_c__AddObject_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  object_recognition_interfaces__srv__AddObject_Request__rosidl_typesupport_introspection_c__AddObject_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t object_recognition_interfaces__srv__AddObject_Request__rosidl_typesupport_introspection_c__AddObject_Request_message_type_support_handle = {
  0,
  &object_recognition_interfaces__srv__AddObject_Request__rosidl_typesupport_introspection_c__AddObject_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_object_recognition_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, object_recognition_interfaces, srv, AddObject_Request)() {
  if (!object_recognition_interfaces__srv__AddObject_Request__rosidl_typesupport_introspection_c__AddObject_Request_message_type_support_handle.typesupport_identifier) {
    object_recognition_interfaces__srv__AddObject_Request__rosidl_typesupport_introspection_c__AddObject_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &object_recognition_interfaces__srv__AddObject_Request__rosidl_typesupport_introspection_c__AddObject_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "object_recognition_interfaces/srv/detail/add_object__rosidl_typesupport_introspection_c.h"
// already included above
// #include "object_recognition_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "object_recognition_interfaces/srv/detail/add_object__functions.h"
// already included above
// #include "object_recognition_interfaces/srv/detail/add_object__struct.h"


// Include directives for member types
// Member `message`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void object_recognition_interfaces__srv__AddObject_Response__rosidl_typesupport_introspection_c__AddObject_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  object_recognition_interfaces__srv__AddObject_Response__init(message_memory);
}

void object_recognition_interfaces__srv__AddObject_Response__rosidl_typesupport_introspection_c__AddObject_Response_fini_function(void * message_memory)
{
  object_recognition_interfaces__srv__AddObject_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember object_recognition_interfaces__srv__AddObject_Response__rosidl_typesupport_introspection_c__AddObject_Response_message_member_array[2] = {
  {
    "success",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(object_recognition_interfaces__srv__AddObject_Response, success),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "message",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(object_recognition_interfaces__srv__AddObject_Response, message),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers object_recognition_interfaces__srv__AddObject_Response__rosidl_typesupport_introspection_c__AddObject_Response_message_members = {
  "object_recognition_interfaces__srv",  // message namespace
  "AddObject_Response",  // message name
  2,  // number of fields
  sizeof(object_recognition_interfaces__srv__AddObject_Response),
  object_recognition_interfaces__srv__AddObject_Response__rosidl_typesupport_introspection_c__AddObject_Response_message_member_array,  // message members
  object_recognition_interfaces__srv__AddObject_Response__rosidl_typesupport_introspection_c__AddObject_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  object_recognition_interfaces__srv__AddObject_Response__rosidl_typesupport_introspection_c__AddObject_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t object_recognition_interfaces__srv__AddObject_Response__rosidl_typesupport_introspection_c__AddObject_Response_message_type_support_handle = {
  0,
  &object_recognition_interfaces__srv__AddObject_Response__rosidl_typesupport_introspection_c__AddObject_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_object_recognition_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, object_recognition_interfaces, srv, AddObject_Response)() {
  if (!object_recognition_interfaces__srv__AddObject_Response__rosidl_typesupport_introspection_c__AddObject_Response_message_type_support_handle.typesupport_identifier) {
    object_recognition_interfaces__srv__AddObject_Response__rosidl_typesupport_introspection_c__AddObject_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &object_recognition_interfaces__srv__AddObject_Response__rosidl_typesupport_introspection_c__AddObject_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "object_recognition_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "object_recognition_interfaces/srv/detail/add_object__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers object_recognition_interfaces__srv__detail__add_object__rosidl_typesupport_introspection_c__AddObject_service_members = {
  "object_recognition_interfaces__srv",  // service namespace
  "AddObject",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // object_recognition_interfaces__srv__detail__add_object__rosidl_typesupport_introspection_c__AddObject_Request_message_type_support_handle,
  NULL  // response message
  // object_recognition_interfaces__srv__detail__add_object__rosidl_typesupport_introspection_c__AddObject_Response_message_type_support_handle
};

static rosidl_service_type_support_t object_recognition_interfaces__srv__detail__add_object__rosidl_typesupport_introspection_c__AddObject_service_type_support_handle = {
  0,
  &object_recognition_interfaces__srv__detail__add_object__rosidl_typesupport_introspection_c__AddObject_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, object_recognition_interfaces, srv, AddObject_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, object_recognition_interfaces, srv, AddObject_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_object_recognition_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, object_recognition_interfaces, srv, AddObject)() {
  if (!object_recognition_interfaces__srv__detail__add_object__rosidl_typesupport_introspection_c__AddObject_service_type_support_handle.typesupport_identifier) {
    object_recognition_interfaces__srv__detail__add_object__rosidl_typesupport_introspection_c__AddObject_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)object_recognition_interfaces__srv__detail__add_object__rosidl_typesupport_introspection_c__AddObject_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, object_recognition_interfaces, srv, AddObject_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, object_recognition_interfaces, srv, AddObject_Response)()->data;
  }

  return &object_recognition_interfaces__srv__detail__add_object__rosidl_typesupport_introspection_c__AddObject_service_type_support_handle;
}

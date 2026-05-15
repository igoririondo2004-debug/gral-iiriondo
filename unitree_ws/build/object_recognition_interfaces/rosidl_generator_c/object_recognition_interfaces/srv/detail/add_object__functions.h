// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from object_recognition_interfaces:srv/AddObject.idl
// generated code does not contain a copyright notice

#ifndef OBJECT_RECOGNITION_INTERFACES__SRV__DETAIL__ADD_OBJECT__FUNCTIONS_H_
#define OBJECT_RECOGNITION_INTERFACES__SRV__DETAIL__ADD_OBJECT__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "object_recognition_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "object_recognition_interfaces/srv/detail/add_object__struct.h"

/// Initialize srv/AddObject message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * object_recognition_interfaces__srv__AddObject_Request
 * )) before or use
 * object_recognition_interfaces__srv__AddObject_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
bool
object_recognition_interfaces__srv__AddObject_Request__init(object_recognition_interfaces__srv__AddObject_Request * msg);

/// Finalize srv/AddObject message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
void
object_recognition_interfaces__srv__AddObject_Request__fini(object_recognition_interfaces__srv__AddObject_Request * msg);

/// Create srv/AddObject message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * object_recognition_interfaces__srv__AddObject_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
object_recognition_interfaces__srv__AddObject_Request *
object_recognition_interfaces__srv__AddObject_Request__create();

/// Destroy srv/AddObject message.
/**
 * It calls
 * object_recognition_interfaces__srv__AddObject_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
void
object_recognition_interfaces__srv__AddObject_Request__destroy(object_recognition_interfaces__srv__AddObject_Request * msg);

/// Check for srv/AddObject message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
bool
object_recognition_interfaces__srv__AddObject_Request__are_equal(const object_recognition_interfaces__srv__AddObject_Request * lhs, const object_recognition_interfaces__srv__AddObject_Request * rhs);

/// Copy a srv/AddObject message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
bool
object_recognition_interfaces__srv__AddObject_Request__copy(
  const object_recognition_interfaces__srv__AddObject_Request * input,
  object_recognition_interfaces__srv__AddObject_Request * output);

/// Initialize array of srv/AddObject messages.
/**
 * It allocates the memory for the number of elements and calls
 * object_recognition_interfaces__srv__AddObject_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
bool
object_recognition_interfaces__srv__AddObject_Request__Sequence__init(object_recognition_interfaces__srv__AddObject_Request__Sequence * array, size_t size);

/// Finalize array of srv/AddObject messages.
/**
 * It calls
 * object_recognition_interfaces__srv__AddObject_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
void
object_recognition_interfaces__srv__AddObject_Request__Sequence__fini(object_recognition_interfaces__srv__AddObject_Request__Sequence * array);

/// Create array of srv/AddObject messages.
/**
 * It allocates the memory for the array and calls
 * object_recognition_interfaces__srv__AddObject_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
object_recognition_interfaces__srv__AddObject_Request__Sequence *
object_recognition_interfaces__srv__AddObject_Request__Sequence__create(size_t size);

/// Destroy array of srv/AddObject messages.
/**
 * It calls
 * object_recognition_interfaces__srv__AddObject_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
void
object_recognition_interfaces__srv__AddObject_Request__Sequence__destroy(object_recognition_interfaces__srv__AddObject_Request__Sequence * array);

/// Check for srv/AddObject message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
bool
object_recognition_interfaces__srv__AddObject_Request__Sequence__are_equal(const object_recognition_interfaces__srv__AddObject_Request__Sequence * lhs, const object_recognition_interfaces__srv__AddObject_Request__Sequence * rhs);

/// Copy an array of srv/AddObject messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
bool
object_recognition_interfaces__srv__AddObject_Request__Sequence__copy(
  const object_recognition_interfaces__srv__AddObject_Request__Sequence * input,
  object_recognition_interfaces__srv__AddObject_Request__Sequence * output);

/// Initialize srv/AddObject message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * object_recognition_interfaces__srv__AddObject_Response
 * )) before or use
 * object_recognition_interfaces__srv__AddObject_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
bool
object_recognition_interfaces__srv__AddObject_Response__init(object_recognition_interfaces__srv__AddObject_Response * msg);

/// Finalize srv/AddObject message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
void
object_recognition_interfaces__srv__AddObject_Response__fini(object_recognition_interfaces__srv__AddObject_Response * msg);

/// Create srv/AddObject message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * object_recognition_interfaces__srv__AddObject_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
object_recognition_interfaces__srv__AddObject_Response *
object_recognition_interfaces__srv__AddObject_Response__create();

/// Destroy srv/AddObject message.
/**
 * It calls
 * object_recognition_interfaces__srv__AddObject_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
void
object_recognition_interfaces__srv__AddObject_Response__destroy(object_recognition_interfaces__srv__AddObject_Response * msg);

/// Check for srv/AddObject message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
bool
object_recognition_interfaces__srv__AddObject_Response__are_equal(const object_recognition_interfaces__srv__AddObject_Response * lhs, const object_recognition_interfaces__srv__AddObject_Response * rhs);

/// Copy a srv/AddObject message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
bool
object_recognition_interfaces__srv__AddObject_Response__copy(
  const object_recognition_interfaces__srv__AddObject_Response * input,
  object_recognition_interfaces__srv__AddObject_Response * output);

/// Initialize array of srv/AddObject messages.
/**
 * It allocates the memory for the number of elements and calls
 * object_recognition_interfaces__srv__AddObject_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
bool
object_recognition_interfaces__srv__AddObject_Response__Sequence__init(object_recognition_interfaces__srv__AddObject_Response__Sequence * array, size_t size);

/// Finalize array of srv/AddObject messages.
/**
 * It calls
 * object_recognition_interfaces__srv__AddObject_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
void
object_recognition_interfaces__srv__AddObject_Response__Sequence__fini(object_recognition_interfaces__srv__AddObject_Response__Sequence * array);

/// Create array of srv/AddObject messages.
/**
 * It allocates the memory for the array and calls
 * object_recognition_interfaces__srv__AddObject_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
object_recognition_interfaces__srv__AddObject_Response__Sequence *
object_recognition_interfaces__srv__AddObject_Response__Sequence__create(size_t size);

/// Destroy array of srv/AddObject messages.
/**
 * It calls
 * object_recognition_interfaces__srv__AddObject_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
void
object_recognition_interfaces__srv__AddObject_Response__Sequence__destroy(object_recognition_interfaces__srv__AddObject_Response__Sequence * array);

/// Check for srv/AddObject message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
bool
object_recognition_interfaces__srv__AddObject_Response__Sequence__are_equal(const object_recognition_interfaces__srv__AddObject_Response__Sequence * lhs, const object_recognition_interfaces__srv__AddObject_Response__Sequence * rhs);

/// Copy an array of srv/AddObject messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_object_recognition_interfaces
bool
object_recognition_interfaces__srv__AddObject_Response__Sequence__copy(
  const object_recognition_interfaces__srv__AddObject_Response__Sequence * input,
  object_recognition_interfaces__srv__AddObject_Response__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // OBJECT_RECOGNITION_INTERFACES__SRV__DETAIL__ADD_OBJECT__FUNCTIONS_H_

// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from speech_to_goal_interfaces:srv/DetectIntent.idl
// generated code does not contain a copyright notice

#ifndef SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__DETECT_INTENT__FUNCTIONS_H_
#define SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__DETECT_INTENT__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "speech_to_goal_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "speech_to_goal_interfaces/srv/detail/detect_intent__struct.h"

/// Initialize srv/DetectIntent message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * speech_to_goal_interfaces__srv__DetectIntent_Request
 * )) before or use
 * speech_to_goal_interfaces__srv__DetectIntent_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
bool
speech_to_goal_interfaces__srv__DetectIntent_Request__init(speech_to_goal_interfaces__srv__DetectIntent_Request * msg);

/// Finalize srv/DetectIntent message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
void
speech_to_goal_interfaces__srv__DetectIntent_Request__fini(speech_to_goal_interfaces__srv__DetectIntent_Request * msg);

/// Create srv/DetectIntent message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * speech_to_goal_interfaces__srv__DetectIntent_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
speech_to_goal_interfaces__srv__DetectIntent_Request *
speech_to_goal_interfaces__srv__DetectIntent_Request__create();

/// Destroy srv/DetectIntent message.
/**
 * It calls
 * speech_to_goal_interfaces__srv__DetectIntent_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
void
speech_to_goal_interfaces__srv__DetectIntent_Request__destroy(speech_to_goal_interfaces__srv__DetectIntent_Request * msg);

/// Check for srv/DetectIntent message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
bool
speech_to_goal_interfaces__srv__DetectIntent_Request__are_equal(const speech_to_goal_interfaces__srv__DetectIntent_Request * lhs, const speech_to_goal_interfaces__srv__DetectIntent_Request * rhs);

/// Copy a srv/DetectIntent message.
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
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
bool
speech_to_goal_interfaces__srv__DetectIntent_Request__copy(
  const speech_to_goal_interfaces__srv__DetectIntent_Request * input,
  speech_to_goal_interfaces__srv__DetectIntent_Request * output);

/// Initialize array of srv/DetectIntent messages.
/**
 * It allocates the memory for the number of elements and calls
 * speech_to_goal_interfaces__srv__DetectIntent_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
bool
speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence__init(speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence * array, size_t size);

/// Finalize array of srv/DetectIntent messages.
/**
 * It calls
 * speech_to_goal_interfaces__srv__DetectIntent_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
void
speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence__fini(speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence * array);

/// Create array of srv/DetectIntent messages.
/**
 * It allocates the memory for the array and calls
 * speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence *
speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence__create(size_t size);

/// Destroy array of srv/DetectIntent messages.
/**
 * It calls
 * speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
void
speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence__destroy(speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence * array);

/// Check for srv/DetectIntent message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
bool
speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence__are_equal(const speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence * lhs, const speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence * rhs);

/// Copy an array of srv/DetectIntent messages.
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
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
bool
speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence__copy(
  const speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence * input,
  speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence * output);

/// Initialize srv/DetectIntent message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * speech_to_goal_interfaces__srv__DetectIntent_Response
 * )) before or use
 * speech_to_goal_interfaces__srv__DetectIntent_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
bool
speech_to_goal_interfaces__srv__DetectIntent_Response__init(speech_to_goal_interfaces__srv__DetectIntent_Response * msg);

/// Finalize srv/DetectIntent message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
void
speech_to_goal_interfaces__srv__DetectIntent_Response__fini(speech_to_goal_interfaces__srv__DetectIntent_Response * msg);

/// Create srv/DetectIntent message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * speech_to_goal_interfaces__srv__DetectIntent_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
speech_to_goal_interfaces__srv__DetectIntent_Response *
speech_to_goal_interfaces__srv__DetectIntent_Response__create();

/// Destroy srv/DetectIntent message.
/**
 * It calls
 * speech_to_goal_interfaces__srv__DetectIntent_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
void
speech_to_goal_interfaces__srv__DetectIntent_Response__destroy(speech_to_goal_interfaces__srv__DetectIntent_Response * msg);

/// Check for srv/DetectIntent message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
bool
speech_to_goal_interfaces__srv__DetectIntent_Response__are_equal(const speech_to_goal_interfaces__srv__DetectIntent_Response * lhs, const speech_to_goal_interfaces__srv__DetectIntent_Response * rhs);

/// Copy a srv/DetectIntent message.
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
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
bool
speech_to_goal_interfaces__srv__DetectIntent_Response__copy(
  const speech_to_goal_interfaces__srv__DetectIntent_Response * input,
  speech_to_goal_interfaces__srv__DetectIntent_Response * output);

/// Initialize array of srv/DetectIntent messages.
/**
 * It allocates the memory for the number of elements and calls
 * speech_to_goal_interfaces__srv__DetectIntent_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
bool
speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence__init(speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence * array, size_t size);

/// Finalize array of srv/DetectIntent messages.
/**
 * It calls
 * speech_to_goal_interfaces__srv__DetectIntent_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
void
speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence__fini(speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence * array);

/// Create array of srv/DetectIntent messages.
/**
 * It allocates the memory for the array and calls
 * speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence *
speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence__create(size_t size);

/// Destroy array of srv/DetectIntent messages.
/**
 * It calls
 * speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
void
speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence__destroy(speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence * array);

/// Check for srv/DetectIntent message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
bool
speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence__are_equal(const speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence * lhs, const speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence * rhs);

/// Copy an array of srv/DetectIntent messages.
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
ROSIDL_GENERATOR_C_PUBLIC_speech_to_goal_interfaces
bool
speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence__copy(
  const speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence * input,
  speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__DETECT_INTENT__FUNCTIONS_H_

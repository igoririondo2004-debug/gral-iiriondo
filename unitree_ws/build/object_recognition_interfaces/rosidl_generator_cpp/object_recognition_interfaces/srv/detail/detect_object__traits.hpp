// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from object_recognition_interfaces:srv/DetectObject.idl
// generated code does not contain a copyright notice

#ifndef OBJECT_RECOGNITION_INTERFACES__SRV__DETAIL__DETECT_OBJECT__TRAITS_HPP_
#define OBJECT_RECOGNITION_INTERFACES__SRV__DETAIL__DETECT_OBJECT__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "object_recognition_interfaces/srv/detail/detect_object__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace object_recognition_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const DetectObject_Request & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DetectObject_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DetectObject_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace object_recognition_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use object_recognition_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const object_recognition_interfaces::srv::DetectObject_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  object_recognition_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use object_recognition_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const object_recognition_interfaces::srv::DetectObject_Request & msg)
{
  return object_recognition_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<object_recognition_interfaces::srv::DetectObject_Request>()
{
  return "object_recognition_interfaces::srv::DetectObject_Request";
}

template<>
inline const char * name<object_recognition_interfaces::srv::DetectObject_Request>()
{
  return "object_recognition_interfaces/srv/DetectObject_Request";
}

template<>
struct has_fixed_size<object_recognition_interfaces::srv::DetectObject_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<object_recognition_interfaces::srv::DetectObject_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<object_recognition_interfaces::srv::DetectObject_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace object_recognition_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const DetectObject_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: object
  {
    out << "object: ";
    rosidl_generator_traits::value_to_yaml(msg.object, out);
    out << ", ";
  }

  // member: confidence
  {
    out << "confidence: ";
    rosidl_generator_traits::value_to_yaml(msg.confidence, out);
    out << ", ";
  }

  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DetectObject_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: object
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "object: ";
    rosidl_generator_traits::value_to_yaml(msg.object, out);
    out << "\n";
  }

  // member: confidence
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "confidence: ";
    rosidl_generator_traits::value_to_yaml(msg.confidence, out);
    out << "\n";
  }

  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DetectObject_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace object_recognition_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use object_recognition_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const object_recognition_interfaces::srv::DetectObject_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  object_recognition_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use object_recognition_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const object_recognition_interfaces::srv::DetectObject_Response & msg)
{
  return object_recognition_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<object_recognition_interfaces::srv::DetectObject_Response>()
{
  return "object_recognition_interfaces::srv::DetectObject_Response";
}

template<>
inline const char * name<object_recognition_interfaces::srv::DetectObject_Response>()
{
  return "object_recognition_interfaces/srv/DetectObject_Response";
}

template<>
struct has_fixed_size<object_recognition_interfaces::srv::DetectObject_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<object_recognition_interfaces::srv::DetectObject_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<object_recognition_interfaces::srv::DetectObject_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<object_recognition_interfaces::srv::DetectObject>()
{
  return "object_recognition_interfaces::srv::DetectObject";
}

template<>
inline const char * name<object_recognition_interfaces::srv::DetectObject>()
{
  return "object_recognition_interfaces/srv/DetectObject";
}

template<>
struct has_fixed_size<object_recognition_interfaces::srv::DetectObject>
  : std::integral_constant<
    bool,
    has_fixed_size<object_recognition_interfaces::srv::DetectObject_Request>::value &&
    has_fixed_size<object_recognition_interfaces::srv::DetectObject_Response>::value
  >
{
};

template<>
struct has_bounded_size<object_recognition_interfaces::srv::DetectObject>
  : std::integral_constant<
    bool,
    has_bounded_size<object_recognition_interfaces::srv::DetectObject_Request>::value &&
    has_bounded_size<object_recognition_interfaces::srv::DetectObject_Response>::value
  >
{
};

template<>
struct is_service<object_recognition_interfaces::srv::DetectObject>
  : std::true_type
{
};

template<>
struct is_service_request<object_recognition_interfaces::srv::DetectObject_Request>
  : std::true_type
{
};

template<>
struct is_service_response<object_recognition_interfaces::srv::DetectObject_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // OBJECT_RECOGNITION_INTERFACES__SRV__DETAIL__DETECT_OBJECT__TRAITS_HPP_

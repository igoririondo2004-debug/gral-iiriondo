// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from object_recognition_interfaces:srv/AddObject.idl
// generated code does not contain a copyright notice

#ifndef OBJECT_RECOGNITION_INTERFACES__SRV__DETAIL__ADD_OBJECT__TRAITS_HPP_
#define OBJECT_RECOGNITION_INTERFACES__SRV__DETAIL__ADD_OBJECT__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "object_recognition_interfaces/srv/detail/add_object__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace object_recognition_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const AddObject_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: name
  {
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
    out << ", ";
  }

  // member: x
  {
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << ", ";
  }

  // member: y
  {
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << ", ";
  }

  // member: z
  {
    out << "z: ";
    rosidl_generator_traits::value_to_yaml(msg.z, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AddObject_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
    out << "\n";
  }

  // member: x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << "\n";
  }

  // member: y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << "\n";
  }

  // member: z
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "z: ";
    rosidl_generator_traits::value_to_yaml(msg.z, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AddObject_Request & msg, bool use_flow_style = false)
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
  const object_recognition_interfaces::srv::AddObject_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  object_recognition_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use object_recognition_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const object_recognition_interfaces::srv::AddObject_Request & msg)
{
  return object_recognition_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<object_recognition_interfaces::srv::AddObject_Request>()
{
  return "object_recognition_interfaces::srv::AddObject_Request";
}

template<>
inline const char * name<object_recognition_interfaces::srv::AddObject_Request>()
{
  return "object_recognition_interfaces/srv/AddObject_Request";
}

template<>
struct has_fixed_size<object_recognition_interfaces::srv::AddObject_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<object_recognition_interfaces::srv::AddObject_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<object_recognition_interfaces::srv::AddObject_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace object_recognition_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const AddObject_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << ", ";
  }

  // member: message
  {
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AddObject_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }

  // member: message
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AddObject_Response & msg, bool use_flow_style = false)
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
  const object_recognition_interfaces::srv::AddObject_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  object_recognition_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use object_recognition_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const object_recognition_interfaces::srv::AddObject_Response & msg)
{
  return object_recognition_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<object_recognition_interfaces::srv::AddObject_Response>()
{
  return "object_recognition_interfaces::srv::AddObject_Response";
}

template<>
inline const char * name<object_recognition_interfaces::srv::AddObject_Response>()
{
  return "object_recognition_interfaces/srv/AddObject_Response";
}

template<>
struct has_fixed_size<object_recognition_interfaces::srv::AddObject_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<object_recognition_interfaces::srv::AddObject_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<object_recognition_interfaces::srv::AddObject_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<object_recognition_interfaces::srv::AddObject>()
{
  return "object_recognition_interfaces::srv::AddObject";
}

template<>
inline const char * name<object_recognition_interfaces::srv::AddObject>()
{
  return "object_recognition_interfaces/srv/AddObject";
}

template<>
struct has_fixed_size<object_recognition_interfaces::srv::AddObject>
  : std::integral_constant<
    bool,
    has_fixed_size<object_recognition_interfaces::srv::AddObject_Request>::value &&
    has_fixed_size<object_recognition_interfaces::srv::AddObject_Response>::value
  >
{
};

template<>
struct has_bounded_size<object_recognition_interfaces::srv::AddObject>
  : std::integral_constant<
    bool,
    has_bounded_size<object_recognition_interfaces::srv::AddObject_Request>::value &&
    has_bounded_size<object_recognition_interfaces::srv::AddObject_Response>::value
  >
{
};

template<>
struct is_service<object_recognition_interfaces::srv::AddObject>
  : std::true_type
{
};

template<>
struct is_service_request<object_recognition_interfaces::srv::AddObject_Request>
  : std::true_type
{
};

template<>
struct is_service_response<object_recognition_interfaces::srv::AddObject_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // OBJECT_RECOGNITION_INTERFACES__SRV__DETAIL__ADD_OBJECT__TRAITS_HPP_

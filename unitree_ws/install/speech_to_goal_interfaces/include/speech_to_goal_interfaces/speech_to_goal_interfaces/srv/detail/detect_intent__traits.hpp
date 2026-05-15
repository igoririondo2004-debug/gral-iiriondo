// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from speech_to_goal_interfaces:srv/DetectIntent.idl
// generated code does not contain a copyright notice

#ifndef SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__DETECT_INTENT__TRAITS_HPP_
#define SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__DETECT_INTENT__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "speech_to_goal_interfaces/srv/detail/detect_intent__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace speech_to_goal_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const DetectIntent_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: text
  {
    out << "text: ";
    rosidl_generator_traits::value_to_yaml(msg.text, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DetectIntent_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: text
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "text: ";
    rosidl_generator_traits::value_to_yaml(msg.text, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DetectIntent_Request & msg, bool use_flow_style = false)
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

}  // namespace speech_to_goal_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use speech_to_goal_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const speech_to_goal_interfaces::srv::DetectIntent_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  speech_to_goal_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use speech_to_goal_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const speech_to_goal_interfaces::srv::DetectIntent_Request & msg)
{
  return speech_to_goal_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<speech_to_goal_interfaces::srv::DetectIntent_Request>()
{
  return "speech_to_goal_interfaces::srv::DetectIntent_Request";
}

template<>
inline const char * name<speech_to_goal_interfaces::srv::DetectIntent_Request>()
{
  return "speech_to_goal_interfaces/srv/DetectIntent_Request";
}

template<>
struct has_fixed_size<speech_to_goal_interfaces::srv::DetectIntent_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<speech_to_goal_interfaces::srv::DetectIntent_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<speech_to_goal_interfaces::srv::DetectIntent_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace speech_to_goal_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const DetectIntent_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: intent
  {
    out << "intent: ";
    rosidl_generator_traits::value_to_yaml(msg.intent, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DetectIntent_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: intent
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "intent: ";
    rosidl_generator_traits::value_to_yaml(msg.intent, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DetectIntent_Response & msg, bool use_flow_style = false)
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

}  // namespace speech_to_goal_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use speech_to_goal_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const speech_to_goal_interfaces::srv::DetectIntent_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  speech_to_goal_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use speech_to_goal_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const speech_to_goal_interfaces::srv::DetectIntent_Response & msg)
{
  return speech_to_goal_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<speech_to_goal_interfaces::srv::DetectIntent_Response>()
{
  return "speech_to_goal_interfaces::srv::DetectIntent_Response";
}

template<>
inline const char * name<speech_to_goal_interfaces::srv::DetectIntent_Response>()
{
  return "speech_to_goal_interfaces/srv/DetectIntent_Response";
}

template<>
struct has_fixed_size<speech_to_goal_interfaces::srv::DetectIntent_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<speech_to_goal_interfaces::srv::DetectIntent_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<speech_to_goal_interfaces::srv::DetectIntent_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<speech_to_goal_interfaces::srv::DetectIntent>()
{
  return "speech_to_goal_interfaces::srv::DetectIntent";
}

template<>
inline const char * name<speech_to_goal_interfaces::srv::DetectIntent>()
{
  return "speech_to_goal_interfaces/srv/DetectIntent";
}

template<>
struct has_fixed_size<speech_to_goal_interfaces::srv::DetectIntent>
  : std::integral_constant<
    bool,
    has_fixed_size<speech_to_goal_interfaces::srv::DetectIntent_Request>::value &&
    has_fixed_size<speech_to_goal_interfaces::srv::DetectIntent_Response>::value
  >
{
};

template<>
struct has_bounded_size<speech_to_goal_interfaces::srv::DetectIntent>
  : std::integral_constant<
    bool,
    has_bounded_size<speech_to_goal_interfaces::srv::DetectIntent_Request>::value &&
    has_bounded_size<speech_to_goal_interfaces::srv::DetectIntent_Response>::value
  >
{
};

template<>
struct is_service<speech_to_goal_interfaces::srv::DetectIntent>
  : std::true_type
{
};

template<>
struct is_service_request<speech_to_goal_interfaces::srv::DetectIntent_Request>
  : std::true_type
{
};

template<>
struct is_service_response<speech_to_goal_interfaces::srv::DetectIntent_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__DETECT_INTENT__TRAITS_HPP_

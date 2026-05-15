// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from speech_to_goal_interfaces:srv/LLMQuery.idl
// generated code does not contain a copyright notice

#ifndef SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__LLM_QUERY__TRAITS_HPP_
#define SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__LLM_QUERY__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "speech_to_goal_interfaces/srv/detail/llm_query__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace speech_to_goal_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const LLMQuery_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: query
  {
    out << "query: ";
    rosidl_generator_traits::value_to_yaml(msg.query, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const LLMQuery_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: query
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "query: ";
    rosidl_generator_traits::value_to_yaml(msg.query, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const LLMQuery_Request & msg, bool use_flow_style = false)
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
  const speech_to_goal_interfaces::srv::LLMQuery_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  speech_to_goal_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use speech_to_goal_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const speech_to_goal_interfaces::srv::LLMQuery_Request & msg)
{
  return speech_to_goal_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<speech_to_goal_interfaces::srv::LLMQuery_Request>()
{
  return "speech_to_goal_interfaces::srv::LLMQuery_Request";
}

template<>
inline const char * name<speech_to_goal_interfaces::srv::LLMQuery_Request>()
{
  return "speech_to_goal_interfaces/srv/LLMQuery_Request";
}

template<>
struct has_fixed_size<speech_to_goal_interfaces::srv::LLMQuery_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<speech_to_goal_interfaces::srv::LLMQuery_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<speech_to_goal_interfaces::srv::LLMQuery_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'waypoints'
#include "speech_to_goal_interfaces/msg/detail/waypoint__traits.hpp"

namespace speech_to_goal_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const LLMQuery_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: waypoints
  {
    if (msg.waypoints.size() == 0) {
      out << "waypoints: []";
    } else {
      out << "waypoints: [";
      size_t pending_items = msg.waypoints.size();
      for (auto item : msg.waypoints) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

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
  const LLMQuery_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: waypoints
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.waypoints.size() == 0) {
      out << "waypoints: []\n";
    } else {
      out << "waypoints:\n";
      for (auto item : msg.waypoints) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
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

inline std::string to_yaml(const LLMQuery_Response & msg, bool use_flow_style = false)
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
  const speech_to_goal_interfaces::srv::LLMQuery_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  speech_to_goal_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use speech_to_goal_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const speech_to_goal_interfaces::srv::LLMQuery_Response & msg)
{
  return speech_to_goal_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<speech_to_goal_interfaces::srv::LLMQuery_Response>()
{
  return "speech_to_goal_interfaces::srv::LLMQuery_Response";
}

template<>
inline const char * name<speech_to_goal_interfaces::srv::LLMQuery_Response>()
{
  return "speech_to_goal_interfaces/srv/LLMQuery_Response";
}

template<>
struct has_fixed_size<speech_to_goal_interfaces::srv::LLMQuery_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<speech_to_goal_interfaces::srv::LLMQuery_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<speech_to_goal_interfaces::srv::LLMQuery_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<speech_to_goal_interfaces::srv::LLMQuery>()
{
  return "speech_to_goal_interfaces::srv::LLMQuery";
}

template<>
inline const char * name<speech_to_goal_interfaces::srv::LLMQuery>()
{
  return "speech_to_goal_interfaces/srv/LLMQuery";
}

template<>
struct has_fixed_size<speech_to_goal_interfaces::srv::LLMQuery>
  : std::integral_constant<
    bool,
    has_fixed_size<speech_to_goal_interfaces::srv::LLMQuery_Request>::value &&
    has_fixed_size<speech_to_goal_interfaces::srv::LLMQuery_Response>::value
  >
{
};

template<>
struct has_bounded_size<speech_to_goal_interfaces::srv::LLMQuery>
  : std::integral_constant<
    bool,
    has_bounded_size<speech_to_goal_interfaces::srv::LLMQuery_Request>::value &&
    has_bounded_size<speech_to_goal_interfaces::srv::LLMQuery_Response>::value
  >
{
};

template<>
struct is_service<speech_to_goal_interfaces::srv::LLMQuery>
  : std::true_type
{
};

template<>
struct is_service_request<speech_to_goal_interfaces::srv::LLMQuery_Request>
  : std::true_type
{
};

template<>
struct is_service_response<speech_to_goal_interfaces::srv::LLMQuery_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__LLM_QUERY__TRAITS_HPP_

// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from speech_to_goal_interfaces:srv/DetectIntent.idl
// generated code does not contain a copyright notice

#ifndef SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__DETECT_INTENT__BUILDER_HPP_
#define SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__DETECT_INTENT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "speech_to_goal_interfaces/srv/detail/detect_intent__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace speech_to_goal_interfaces
{

namespace srv
{

namespace builder
{

class Init_DetectIntent_Request_text
{
public:
  Init_DetectIntent_Request_text()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::speech_to_goal_interfaces::srv::DetectIntent_Request text(::speech_to_goal_interfaces::srv::DetectIntent_Request::_text_type arg)
  {
    msg_.text = std::move(arg);
    return std::move(msg_);
  }

private:
  ::speech_to_goal_interfaces::srv::DetectIntent_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::speech_to_goal_interfaces::srv::DetectIntent_Request>()
{
  return speech_to_goal_interfaces::srv::builder::Init_DetectIntent_Request_text();
}

}  // namespace speech_to_goal_interfaces


namespace speech_to_goal_interfaces
{

namespace srv
{

namespace builder
{

class Init_DetectIntent_Response_intent
{
public:
  Init_DetectIntent_Response_intent()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::speech_to_goal_interfaces::srv::DetectIntent_Response intent(::speech_to_goal_interfaces::srv::DetectIntent_Response::_intent_type arg)
  {
    msg_.intent = std::move(arg);
    return std::move(msg_);
  }

private:
  ::speech_to_goal_interfaces::srv::DetectIntent_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::speech_to_goal_interfaces::srv::DetectIntent_Response>()
{
  return speech_to_goal_interfaces::srv::builder::Init_DetectIntent_Response_intent();
}

}  // namespace speech_to_goal_interfaces

#endif  // SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__DETECT_INTENT__BUILDER_HPP_

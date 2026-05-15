// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from speech_to_goal_interfaces:srv/LLMQuery.idl
// generated code does not contain a copyright notice

#ifndef SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__LLM_QUERY__BUILDER_HPP_
#define SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__LLM_QUERY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "speech_to_goal_interfaces/srv/detail/llm_query__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace speech_to_goal_interfaces
{

namespace srv
{

namespace builder
{

class Init_LLMQuery_Request_query
{
public:
  Init_LLMQuery_Request_query()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::speech_to_goal_interfaces::srv::LLMQuery_Request query(::speech_to_goal_interfaces::srv::LLMQuery_Request::_query_type arg)
  {
    msg_.query = std::move(arg);
    return std::move(msg_);
  }

private:
  ::speech_to_goal_interfaces::srv::LLMQuery_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::speech_to_goal_interfaces::srv::LLMQuery_Request>()
{
  return speech_to_goal_interfaces::srv::builder::Init_LLMQuery_Request_query();
}

}  // namespace speech_to_goal_interfaces


namespace speech_to_goal_interfaces
{

namespace srv
{

namespace builder
{

class Init_LLMQuery_Response_message
{
public:
  explicit Init_LLMQuery_Response_message(::speech_to_goal_interfaces::srv::LLMQuery_Response & msg)
  : msg_(msg)
  {}
  ::speech_to_goal_interfaces::srv::LLMQuery_Response message(::speech_to_goal_interfaces::srv::LLMQuery_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::speech_to_goal_interfaces::srv::LLMQuery_Response msg_;
};

class Init_LLMQuery_Response_success
{
public:
  explicit Init_LLMQuery_Response_success(::speech_to_goal_interfaces::srv::LLMQuery_Response & msg)
  : msg_(msg)
  {}
  Init_LLMQuery_Response_message success(::speech_to_goal_interfaces::srv::LLMQuery_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_LLMQuery_Response_message(msg_);
  }

private:
  ::speech_to_goal_interfaces::srv::LLMQuery_Response msg_;
};

class Init_LLMQuery_Response_waypoints
{
public:
  Init_LLMQuery_Response_waypoints()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LLMQuery_Response_success waypoints(::speech_to_goal_interfaces::srv::LLMQuery_Response::_waypoints_type arg)
  {
    msg_.waypoints = std::move(arg);
    return Init_LLMQuery_Response_success(msg_);
  }

private:
  ::speech_to_goal_interfaces::srv::LLMQuery_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::speech_to_goal_interfaces::srv::LLMQuery_Response>()
{
  return speech_to_goal_interfaces::srv::builder::Init_LLMQuery_Response_waypoints();
}

}  // namespace speech_to_goal_interfaces

#endif  // SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__LLM_QUERY__BUILDER_HPP_

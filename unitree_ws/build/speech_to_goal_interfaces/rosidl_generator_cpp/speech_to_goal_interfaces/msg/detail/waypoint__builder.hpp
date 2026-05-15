// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from speech_to_goal_interfaces:msg/Waypoint.idl
// generated code does not contain a copyright notice

#ifndef SPEECH_TO_GOAL_INTERFACES__MSG__DETAIL__WAYPOINT__BUILDER_HPP_
#define SPEECH_TO_GOAL_INTERFACES__MSG__DETAIL__WAYPOINT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "speech_to_goal_interfaces/msg/detail/waypoint__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace speech_to_goal_interfaces
{

namespace msg
{

namespace builder
{

class Init_Waypoint_z
{
public:
  explicit Init_Waypoint_z(::speech_to_goal_interfaces::msg::Waypoint & msg)
  : msg_(msg)
  {}
  ::speech_to_goal_interfaces::msg::Waypoint z(::speech_to_goal_interfaces::msg::Waypoint::_z_type arg)
  {
    msg_.z = std::move(arg);
    return std::move(msg_);
  }

private:
  ::speech_to_goal_interfaces::msg::Waypoint msg_;
};

class Init_Waypoint_y
{
public:
  explicit Init_Waypoint_y(::speech_to_goal_interfaces::msg::Waypoint & msg)
  : msg_(msg)
  {}
  Init_Waypoint_z y(::speech_to_goal_interfaces::msg::Waypoint::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_Waypoint_z(msg_);
  }

private:
  ::speech_to_goal_interfaces::msg::Waypoint msg_;
};

class Init_Waypoint_x
{
public:
  explicit Init_Waypoint_x(::speech_to_goal_interfaces::msg::Waypoint & msg)
  : msg_(msg)
  {}
  Init_Waypoint_y x(::speech_to_goal_interfaces::msg::Waypoint::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Waypoint_y(msg_);
  }

private:
  ::speech_to_goal_interfaces::msg::Waypoint msg_;
};

class Init_Waypoint_name
{
public:
  Init_Waypoint_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Waypoint_x name(::speech_to_goal_interfaces::msg::Waypoint::_name_type arg)
  {
    msg_.name = std::move(arg);
    return Init_Waypoint_x(msg_);
  }

private:
  ::speech_to_goal_interfaces::msg::Waypoint msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::speech_to_goal_interfaces::msg::Waypoint>()
{
  return speech_to_goal_interfaces::msg::builder::Init_Waypoint_name();
}

}  // namespace speech_to_goal_interfaces

#endif  // SPEECH_TO_GOAL_INTERFACES__MSG__DETAIL__WAYPOINT__BUILDER_HPP_

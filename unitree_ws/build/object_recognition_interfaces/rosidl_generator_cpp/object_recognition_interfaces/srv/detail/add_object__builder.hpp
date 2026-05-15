// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from object_recognition_interfaces:srv/AddObject.idl
// generated code does not contain a copyright notice

#ifndef OBJECT_RECOGNITION_INTERFACES__SRV__DETAIL__ADD_OBJECT__BUILDER_HPP_
#define OBJECT_RECOGNITION_INTERFACES__SRV__DETAIL__ADD_OBJECT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "object_recognition_interfaces/srv/detail/add_object__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace object_recognition_interfaces
{

namespace srv
{

namespace builder
{

class Init_AddObject_Request_z
{
public:
  explicit Init_AddObject_Request_z(::object_recognition_interfaces::srv::AddObject_Request & msg)
  : msg_(msg)
  {}
  ::object_recognition_interfaces::srv::AddObject_Request z(::object_recognition_interfaces::srv::AddObject_Request::_z_type arg)
  {
    msg_.z = std::move(arg);
    return std::move(msg_);
  }

private:
  ::object_recognition_interfaces::srv::AddObject_Request msg_;
};

class Init_AddObject_Request_y
{
public:
  explicit Init_AddObject_Request_y(::object_recognition_interfaces::srv::AddObject_Request & msg)
  : msg_(msg)
  {}
  Init_AddObject_Request_z y(::object_recognition_interfaces::srv::AddObject_Request::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_AddObject_Request_z(msg_);
  }

private:
  ::object_recognition_interfaces::srv::AddObject_Request msg_;
};

class Init_AddObject_Request_x
{
public:
  explicit Init_AddObject_Request_x(::object_recognition_interfaces::srv::AddObject_Request & msg)
  : msg_(msg)
  {}
  Init_AddObject_Request_y x(::object_recognition_interfaces::srv::AddObject_Request::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_AddObject_Request_y(msg_);
  }

private:
  ::object_recognition_interfaces::srv::AddObject_Request msg_;
};

class Init_AddObject_Request_name
{
public:
  Init_AddObject_Request_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AddObject_Request_x name(::object_recognition_interfaces::srv::AddObject_Request::_name_type arg)
  {
    msg_.name = std::move(arg);
    return Init_AddObject_Request_x(msg_);
  }

private:
  ::object_recognition_interfaces::srv::AddObject_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::object_recognition_interfaces::srv::AddObject_Request>()
{
  return object_recognition_interfaces::srv::builder::Init_AddObject_Request_name();
}

}  // namespace object_recognition_interfaces


namespace object_recognition_interfaces
{

namespace srv
{

namespace builder
{

class Init_AddObject_Response_message
{
public:
  explicit Init_AddObject_Response_message(::object_recognition_interfaces::srv::AddObject_Response & msg)
  : msg_(msg)
  {}
  ::object_recognition_interfaces::srv::AddObject_Response message(::object_recognition_interfaces::srv::AddObject_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::object_recognition_interfaces::srv::AddObject_Response msg_;
};

class Init_AddObject_Response_success
{
public:
  Init_AddObject_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AddObject_Response_message success(::object_recognition_interfaces::srv::AddObject_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_AddObject_Response_message(msg_);
  }

private:
  ::object_recognition_interfaces::srv::AddObject_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::object_recognition_interfaces::srv::AddObject_Response>()
{
  return object_recognition_interfaces::srv::builder::Init_AddObject_Response_success();
}

}  // namespace object_recognition_interfaces

#endif  // OBJECT_RECOGNITION_INTERFACES__SRV__DETAIL__ADD_OBJECT__BUILDER_HPP_

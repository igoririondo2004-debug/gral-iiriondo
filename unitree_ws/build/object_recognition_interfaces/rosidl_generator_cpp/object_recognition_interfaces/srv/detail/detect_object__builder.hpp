// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from object_recognition_interfaces:srv/DetectObject.idl
// generated code does not contain a copyright notice

#ifndef OBJECT_RECOGNITION_INTERFACES__SRV__DETAIL__DETECT_OBJECT__BUILDER_HPP_
#define OBJECT_RECOGNITION_INTERFACES__SRV__DETAIL__DETECT_OBJECT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "object_recognition_interfaces/srv/detail/detect_object__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace object_recognition_interfaces
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::object_recognition_interfaces::srv::DetectObject_Request>()
{
  return ::object_recognition_interfaces::srv::DetectObject_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace object_recognition_interfaces


namespace object_recognition_interfaces
{

namespace srv
{

namespace builder
{

class Init_DetectObject_Response_success
{
public:
  explicit Init_DetectObject_Response_success(::object_recognition_interfaces::srv::DetectObject_Response & msg)
  : msg_(msg)
  {}
  ::object_recognition_interfaces::srv::DetectObject_Response success(::object_recognition_interfaces::srv::DetectObject_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::object_recognition_interfaces::srv::DetectObject_Response msg_;
};

class Init_DetectObject_Response_confidence
{
public:
  explicit Init_DetectObject_Response_confidence(::object_recognition_interfaces::srv::DetectObject_Response & msg)
  : msg_(msg)
  {}
  Init_DetectObject_Response_success confidence(::object_recognition_interfaces::srv::DetectObject_Response::_confidence_type arg)
  {
    msg_.confidence = std::move(arg);
    return Init_DetectObject_Response_success(msg_);
  }

private:
  ::object_recognition_interfaces::srv::DetectObject_Response msg_;
};

class Init_DetectObject_Response_object
{
public:
  Init_DetectObject_Response_object()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DetectObject_Response_confidence object(::object_recognition_interfaces::srv::DetectObject_Response::_object_type arg)
  {
    msg_.object = std::move(arg);
    return Init_DetectObject_Response_confidence(msg_);
  }

private:
  ::object_recognition_interfaces::srv::DetectObject_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::object_recognition_interfaces::srv::DetectObject_Response>()
{
  return object_recognition_interfaces::srv::builder::Init_DetectObject_Response_object();
}

}  // namespace object_recognition_interfaces

#endif  // OBJECT_RECOGNITION_INTERFACES__SRV__DETAIL__DETECT_OBJECT__BUILDER_HPP_

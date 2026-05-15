// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from speech_to_goal_interfaces:srv/LLMQuery.idl
// generated code does not contain a copyright notice

#ifndef SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__LLM_QUERY__STRUCT_HPP_
#define SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__LLM_QUERY__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__speech_to_goal_interfaces__srv__LLMQuery_Request __attribute__((deprecated))
#else
# define DEPRECATED__speech_to_goal_interfaces__srv__LLMQuery_Request __declspec(deprecated)
#endif

namespace speech_to_goal_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct LLMQuery_Request_
{
  using Type = LLMQuery_Request_<ContainerAllocator>;

  explicit LLMQuery_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->query = "";
    }
  }

  explicit LLMQuery_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : query(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->query = "";
    }
  }

  // field types and members
  using _query_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _query_type query;

  // setters for named parameter idiom
  Type & set__query(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->query = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    speech_to_goal_interfaces::srv::LLMQuery_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const speech_to_goal_interfaces::srv::LLMQuery_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<speech_to_goal_interfaces::srv::LLMQuery_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<speech_to_goal_interfaces::srv::LLMQuery_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      speech_to_goal_interfaces::srv::LLMQuery_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<speech_to_goal_interfaces::srv::LLMQuery_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      speech_to_goal_interfaces::srv::LLMQuery_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<speech_to_goal_interfaces::srv::LLMQuery_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<speech_to_goal_interfaces::srv::LLMQuery_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<speech_to_goal_interfaces::srv::LLMQuery_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__speech_to_goal_interfaces__srv__LLMQuery_Request
    std::shared_ptr<speech_to_goal_interfaces::srv::LLMQuery_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__speech_to_goal_interfaces__srv__LLMQuery_Request
    std::shared_ptr<speech_to_goal_interfaces::srv::LLMQuery_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const LLMQuery_Request_ & other) const
  {
    if (this->query != other.query) {
      return false;
    }
    return true;
  }
  bool operator!=(const LLMQuery_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct LLMQuery_Request_

// alias to use template instance with default allocator
using LLMQuery_Request =
  speech_to_goal_interfaces::srv::LLMQuery_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace speech_to_goal_interfaces


// Include directives for member types
// Member 'waypoints'
#include "speech_to_goal_interfaces/msg/detail/waypoint__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__speech_to_goal_interfaces__srv__LLMQuery_Response __attribute__((deprecated))
#else
# define DEPRECATED__speech_to_goal_interfaces__srv__LLMQuery_Response __declspec(deprecated)
#endif

namespace speech_to_goal_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct LLMQuery_Response_
{
  using Type = LLMQuery_Response_<ContainerAllocator>;

  explicit LLMQuery_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
    }
  }

  explicit LLMQuery_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : message(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
    }
  }

  // field types and members
  using _waypoints_type =
    std::vector<speech_to_goal_interfaces::msg::Waypoint_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<speech_to_goal_interfaces::msg::Waypoint_<ContainerAllocator>>>;
  _waypoints_type waypoints;
  using _success_type =
    bool;
  _success_type success;
  using _message_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _message_type message;

  // setters for named parameter idiom
  Type & set__waypoints(
    const std::vector<speech_to_goal_interfaces::msg::Waypoint_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<speech_to_goal_interfaces::msg::Waypoint_<ContainerAllocator>>> & _arg)
  {
    this->waypoints = _arg;
    return *this;
  }
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }
  Type & set__message(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->message = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    speech_to_goal_interfaces::srv::LLMQuery_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const speech_to_goal_interfaces::srv::LLMQuery_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<speech_to_goal_interfaces::srv::LLMQuery_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<speech_to_goal_interfaces::srv::LLMQuery_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      speech_to_goal_interfaces::srv::LLMQuery_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<speech_to_goal_interfaces::srv::LLMQuery_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      speech_to_goal_interfaces::srv::LLMQuery_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<speech_to_goal_interfaces::srv::LLMQuery_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<speech_to_goal_interfaces::srv::LLMQuery_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<speech_to_goal_interfaces::srv::LLMQuery_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__speech_to_goal_interfaces__srv__LLMQuery_Response
    std::shared_ptr<speech_to_goal_interfaces::srv::LLMQuery_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__speech_to_goal_interfaces__srv__LLMQuery_Response
    std::shared_ptr<speech_to_goal_interfaces::srv::LLMQuery_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const LLMQuery_Response_ & other) const
  {
    if (this->waypoints != other.waypoints) {
      return false;
    }
    if (this->success != other.success) {
      return false;
    }
    if (this->message != other.message) {
      return false;
    }
    return true;
  }
  bool operator!=(const LLMQuery_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct LLMQuery_Response_

// alias to use template instance with default allocator
using LLMQuery_Response =
  speech_to_goal_interfaces::srv::LLMQuery_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace speech_to_goal_interfaces

namespace speech_to_goal_interfaces
{

namespace srv
{

struct LLMQuery
{
  using Request = speech_to_goal_interfaces::srv::LLMQuery_Request;
  using Response = speech_to_goal_interfaces::srv::LLMQuery_Response;
};

}  // namespace srv

}  // namespace speech_to_goal_interfaces

#endif  // SPEECH_TO_GOAL_INTERFACES__SRV__DETAIL__LLM_QUERY__STRUCT_HPP_

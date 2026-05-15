// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from object_recognition_interfaces:srv/DetectObject.idl
// generated code does not contain a copyright notice

#ifndef OBJECT_RECOGNITION_INTERFACES__SRV__DETAIL__DETECT_OBJECT__STRUCT_HPP_
#define OBJECT_RECOGNITION_INTERFACES__SRV__DETAIL__DETECT_OBJECT__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__object_recognition_interfaces__srv__DetectObject_Request __attribute__((deprecated))
#else
# define DEPRECATED__object_recognition_interfaces__srv__DetectObject_Request __declspec(deprecated)
#endif

namespace object_recognition_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct DetectObject_Request_
{
  using Type = DetectObject_Request_<ContainerAllocator>;

  explicit DetectObject_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit DetectObject_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  // field types and members
  using _structure_needs_at_least_one_member_type =
    uint8_t;
  _structure_needs_at_least_one_member_type structure_needs_at_least_one_member;


  // constant declarations

  // pointer types
  using RawPtr =
    object_recognition_interfaces::srv::DetectObject_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const object_recognition_interfaces::srv::DetectObject_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<object_recognition_interfaces::srv::DetectObject_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<object_recognition_interfaces::srv::DetectObject_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      object_recognition_interfaces::srv::DetectObject_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<object_recognition_interfaces::srv::DetectObject_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      object_recognition_interfaces::srv::DetectObject_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<object_recognition_interfaces::srv::DetectObject_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<object_recognition_interfaces::srv::DetectObject_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<object_recognition_interfaces::srv::DetectObject_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__object_recognition_interfaces__srv__DetectObject_Request
    std::shared_ptr<object_recognition_interfaces::srv::DetectObject_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__object_recognition_interfaces__srv__DetectObject_Request
    std::shared_ptr<object_recognition_interfaces::srv::DetectObject_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DetectObject_Request_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const DetectObject_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DetectObject_Request_

// alias to use template instance with default allocator
using DetectObject_Request =
  object_recognition_interfaces::srv::DetectObject_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace object_recognition_interfaces


#ifndef _WIN32
# define DEPRECATED__object_recognition_interfaces__srv__DetectObject_Response __attribute__((deprecated))
#else
# define DEPRECATED__object_recognition_interfaces__srv__DetectObject_Response __declspec(deprecated)
#endif

namespace object_recognition_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct DetectObject_Response_
{
  using Type = DetectObject_Response_<ContainerAllocator>;

  explicit DetectObject_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->object = "";
      this->confidence = 0.0f;
      this->success = false;
    }
  }

  explicit DetectObject_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : object(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->object = "";
      this->confidence = 0.0f;
      this->success = false;
    }
  }

  // field types and members
  using _object_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _object_type object;
  using _confidence_type =
    float;
  _confidence_type confidence;
  using _success_type =
    bool;
  _success_type success;

  // setters for named parameter idiom
  Type & set__object(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->object = _arg;
    return *this;
  }
  Type & set__confidence(
    const float & _arg)
  {
    this->confidence = _arg;
    return *this;
  }
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    object_recognition_interfaces::srv::DetectObject_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const object_recognition_interfaces::srv::DetectObject_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<object_recognition_interfaces::srv::DetectObject_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<object_recognition_interfaces::srv::DetectObject_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      object_recognition_interfaces::srv::DetectObject_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<object_recognition_interfaces::srv::DetectObject_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      object_recognition_interfaces::srv::DetectObject_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<object_recognition_interfaces::srv::DetectObject_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<object_recognition_interfaces::srv::DetectObject_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<object_recognition_interfaces::srv::DetectObject_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__object_recognition_interfaces__srv__DetectObject_Response
    std::shared_ptr<object_recognition_interfaces::srv::DetectObject_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__object_recognition_interfaces__srv__DetectObject_Response
    std::shared_ptr<object_recognition_interfaces::srv::DetectObject_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DetectObject_Response_ & other) const
  {
    if (this->object != other.object) {
      return false;
    }
    if (this->confidence != other.confidence) {
      return false;
    }
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const DetectObject_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DetectObject_Response_

// alias to use template instance with default allocator
using DetectObject_Response =
  object_recognition_interfaces::srv::DetectObject_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace object_recognition_interfaces

namespace object_recognition_interfaces
{

namespace srv
{

struct DetectObject
{
  using Request = object_recognition_interfaces::srv::DetectObject_Request;
  using Response = object_recognition_interfaces::srv::DetectObject_Response;
};

}  // namespace srv

}  // namespace object_recognition_interfaces

#endif  // OBJECT_RECOGNITION_INTERFACES__SRV__DETAIL__DETECT_OBJECT__STRUCT_HPP_

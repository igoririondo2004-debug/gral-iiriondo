// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from aruco_markers_msgs:msg/Marker.idl
// generated code does not contain a copyright notice

#ifndef ARUCO_MARKERS_MSGS__MSG__DETAIL__MARKER__STRUCT_HPP_
#define ARUCO_MARKERS_MSGS__MSG__DETAIL__MARKER__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"
// Member 'pose'
#include "geometry_msgs/msg/detail/pose_stamped__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__aruco_markers_msgs__msg__Marker __attribute__((deprecated))
#else
# define DEPRECATED__aruco_markers_msgs__msg__Marker __declspec(deprecated)
#endif

namespace aruco_markers_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Marker_
{
  using Type = Marker_<ContainerAllocator>;

  explicit Marker_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init),
    pose(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->pixel_x = 0.0;
      this->pixel_y = 0.0;
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->id = 0ul;
      this->pixel_x = 0.0;
      this->pixel_y = 0.0;
    }
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0ul;
    }
  }

  explicit Marker_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    pose(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->pixel_x = 0.0;
      this->pixel_y = 0.0;
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->id = 0ul;
      this->pixel_x = 0.0;
      this->pixel_y = 0.0;
    }
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0ul;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _id_type =
    uint32_t;
  _id_type id;
  using _pose_type =
    geometry_msgs::msg::PoseStamped_<ContainerAllocator>;
  _pose_type pose;
  using _pixel_x_type =
    double;
  _pixel_x_type pixel_x;
  using _pixel_y_type =
    double;
  _pixel_y_type pixel_y;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__id(
    const uint32_t & _arg)
  {
    this->id = _arg;
    return *this;
  }
  Type & set__pose(
    const geometry_msgs::msg::PoseStamped_<ContainerAllocator> & _arg)
  {
    this->pose = _arg;
    return *this;
  }
  Type & set__pixel_x(
    const double & _arg)
  {
    this->pixel_x = _arg;
    return *this;
  }
  Type & set__pixel_y(
    const double & _arg)
  {
    this->pixel_y = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    aruco_markers_msgs::msg::Marker_<ContainerAllocator> *;
  using ConstRawPtr =
    const aruco_markers_msgs::msg::Marker_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<aruco_markers_msgs::msg::Marker_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<aruco_markers_msgs::msg::Marker_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      aruco_markers_msgs::msg::Marker_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<aruco_markers_msgs::msg::Marker_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      aruco_markers_msgs::msg::Marker_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<aruco_markers_msgs::msg::Marker_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<aruco_markers_msgs::msg::Marker_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<aruco_markers_msgs::msg::Marker_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__aruco_markers_msgs__msg__Marker
    std::shared_ptr<aruco_markers_msgs::msg::Marker_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__aruco_markers_msgs__msg__Marker
    std::shared_ptr<aruco_markers_msgs::msg::Marker_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Marker_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->id != other.id) {
      return false;
    }
    if (this->pose != other.pose) {
      return false;
    }
    if (this->pixel_x != other.pixel_x) {
      return false;
    }
    if (this->pixel_y != other.pixel_y) {
      return false;
    }
    return true;
  }
  bool operator!=(const Marker_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Marker_

// alias to use template instance with default allocator
using Marker =
  aruco_markers_msgs::msg::Marker_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace aruco_markers_msgs

#endif  // ARUCO_MARKERS_MSGS__MSG__DETAIL__MARKER__STRUCT_HPP_

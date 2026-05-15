#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "speech_to_goal_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__speech_to_goal_interfaces__msg__Waypoint() -> *const std::ffi::c_void;
}

#[link(name = "speech_to_goal_interfaces__rosidl_generator_c")]
extern "C" {
    fn speech_to_goal_interfaces__msg__Waypoint__init(msg: *mut Waypoint) -> bool;
    fn speech_to_goal_interfaces__msg__Waypoint__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Waypoint>, size: usize) -> bool;
    fn speech_to_goal_interfaces__msg__Waypoint__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Waypoint>);
    fn speech_to_goal_interfaces__msg__Waypoint__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Waypoint>, out_seq: *mut rosidl_runtime_rs::Sequence<Waypoint>) -> bool;
}

// Corresponds to speech_to_goal_interfaces__msg__Waypoint
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Waypoint {

    // This member is not documented.
    #[allow(missing_docs)]
    pub name: rosidl_runtime_rs::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub x: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub y: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub z: f64,

}



impl Default for Waypoint {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !speech_to_goal_interfaces__msg__Waypoint__init(&mut msg as *mut _) {
        panic!("Call to speech_to_goal_interfaces__msg__Waypoint__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Waypoint {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { speech_to_goal_interfaces__msg__Waypoint__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { speech_to_goal_interfaces__msg__Waypoint__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { speech_to_goal_interfaces__msg__Waypoint__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Waypoint {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Waypoint where Self: Sized {
  const TYPE_NAME: &'static str = "speech_to_goal_interfaces/msg/Waypoint";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__speech_to_goal_interfaces__msg__Waypoint() }
  }
}



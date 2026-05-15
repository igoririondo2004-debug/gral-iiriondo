#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



#[link(name = "speech_to_goal_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__speech_to_goal_interfaces__srv__LLMQuery_Request() -> *const std::ffi::c_void;
}

#[link(name = "speech_to_goal_interfaces__rosidl_generator_c")]
extern "C" {
    fn speech_to_goal_interfaces__srv__LLMQuery_Request__init(msg: *mut LLMQuery_Request) -> bool;
    fn speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<LLMQuery_Request>, size: usize) -> bool;
    fn speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<LLMQuery_Request>);
    fn speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<LLMQuery_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<LLMQuery_Request>) -> bool;
}

// Corresponds to speech_to_goal_interfaces__srv__LLMQuery_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct LLMQuery_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub query: rosidl_runtime_rs::String,

}



impl Default for LLMQuery_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !speech_to_goal_interfaces__srv__LLMQuery_Request__init(&mut msg as *mut _) {
        panic!("Call to speech_to_goal_interfaces__srv__LLMQuery_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for LLMQuery_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { speech_to_goal_interfaces__srv__LLMQuery_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for LLMQuery_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for LLMQuery_Request where Self: Sized {
  const TYPE_NAME: &'static str = "speech_to_goal_interfaces/srv/LLMQuery_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__speech_to_goal_interfaces__srv__LLMQuery_Request() }
  }
}


#[link(name = "speech_to_goal_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__speech_to_goal_interfaces__srv__LLMQuery_Response() -> *const std::ffi::c_void;
}

#[link(name = "speech_to_goal_interfaces__rosidl_generator_c")]
extern "C" {
    fn speech_to_goal_interfaces__srv__LLMQuery_Response__init(msg: *mut LLMQuery_Response) -> bool;
    fn speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<LLMQuery_Response>, size: usize) -> bool;
    fn speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<LLMQuery_Response>);
    fn speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<LLMQuery_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<LLMQuery_Response>) -> bool;
}

// Corresponds to speech_to_goal_interfaces__srv__LLMQuery_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct LLMQuery_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub waypoints: rosidl_runtime_rs::Sequence<super::super::msg::rmw::Waypoint>,


    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub message: rosidl_runtime_rs::String,

}



impl Default for LLMQuery_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !speech_to_goal_interfaces__srv__LLMQuery_Response__init(&mut msg as *mut _) {
        panic!("Call to speech_to_goal_interfaces__srv__LLMQuery_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for LLMQuery_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { speech_to_goal_interfaces__srv__LLMQuery_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for LLMQuery_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for LLMQuery_Response where Self: Sized {
  const TYPE_NAME: &'static str = "speech_to_goal_interfaces/srv/LLMQuery_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__speech_to_goal_interfaces__srv__LLMQuery_Response() }
  }
}


#[link(name = "speech_to_goal_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__speech_to_goal_interfaces__srv__DetectIntent_Request() -> *const std::ffi::c_void;
}

#[link(name = "speech_to_goal_interfaces__rosidl_generator_c")]
extern "C" {
    fn speech_to_goal_interfaces__srv__DetectIntent_Request__init(msg: *mut DetectIntent_Request) -> bool;
    fn speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DetectIntent_Request>, size: usize) -> bool;
    fn speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DetectIntent_Request>);
    fn speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DetectIntent_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<DetectIntent_Request>) -> bool;
}

// Corresponds to speech_to_goal_interfaces__srv__DetectIntent_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DetectIntent_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub text: rosidl_runtime_rs::String,

}



impl Default for DetectIntent_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !speech_to_goal_interfaces__srv__DetectIntent_Request__init(&mut msg as *mut _) {
        panic!("Call to speech_to_goal_interfaces__srv__DetectIntent_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DetectIntent_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { speech_to_goal_interfaces__srv__DetectIntent_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DetectIntent_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DetectIntent_Request where Self: Sized {
  const TYPE_NAME: &'static str = "speech_to_goal_interfaces/srv/DetectIntent_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__speech_to_goal_interfaces__srv__DetectIntent_Request() }
  }
}


#[link(name = "speech_to_goal_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__speech_to_goal_interfaces__srv__DetectIntent_Response() -> *const std::ffi::c_void;
}

#[link(name = "speech_to_goal_interfaces__rosidl_generator_c")]
extern "C" {
    fn speech_to_goal_interfaces__srv__DetectIntent_Response__init(msg: *mut DetectIntent_Response) -> bool;
    fn speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DetectIntent_Response>, size: usize) -> bool;
    fn speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DetectIntent_Response>);
    fn speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DetectIntent_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<DetectIntent_Response>) -> bool;
}

// Corresponds to speech_to_goal_interfaces__srv__DetectIntent_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DetectIntent_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub intent: rosidl_runtime_rs::String,

}



impl Default for DetectIntent_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !speech_to_goal_interfaces__srv__DetectIntent_Response__init(&mut msg as *mut _) {
        panic!("Call to speech_to_goal_interfaces__srv__DetectIntent_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DetectIntent_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { speech_to_goal_interfaces__srv__DetectIntent_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DetectIntent_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DetectIntent_Response where Self: Sized {
  const TYPE_NAME: &'static str = "speech_to_goal_interfaces/srv/DetectIntent_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__speech_to_goal_interfaces__srv__DetectIntent_Response() }
  }
}






#[link(name = "speech_to_goal_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__speech_to_goal_interfaces__srv__LLMQuery() -> *const std::ffi::c_void;
}

// Corresponds to speech_to_goal_interfaces__srv__LLMQuery
#[allow(missing_docs, non_camel_case_types)]
pub struct LLMQuery;

impl rosidl_runtime_rs::Service for LLMQuery {
    type Request = LLMQuery_Request;
    type Response = LLMQuery_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__speech_to_goal_interfaces__srv__LLMQuery() }
    }
}




#[link(name = "speech_to_goal_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__speech_to_goal_interfaces__srv__DetectIntent() -> *const std::ffi::c_void;
}

// Corresponds to speech_to_goal_interfaces__srv__DetectIntent
#[allow(missing_docs, non_camel_case_types)]
pub struct DetectIntent;

impl rosidl_runtime_rs::Service for DetectIntent {
    type Request = DetectIntent_Request;
    type Response = DetectIntent_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__speech_to_goal_interfaces__srv__DetectIntent() }
    }
}



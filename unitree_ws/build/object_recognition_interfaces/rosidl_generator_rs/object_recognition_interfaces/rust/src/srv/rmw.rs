#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



#[link(name = "object_recognition_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__object_recognition_interfaces__srv__DetectObject_Request() -> *const std::ffi::c_void;
}

#[link(name = "object_recognition_interfaces__rosidl_generator_c")]
extern "C" {
    fn object_recognition_interfaces__srv__DetectObject_Request__init(msg: *mut DetectObject_Request) -> bool;
    fn object_recognition_interfaces__srv__DetectObject_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DetectObject_Request>, size: usize) -> bool;
    fn object_recognition_interfaces__srv__DetectObject_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DetectObject_Request>);
    fn object_recognition_interfaces__srv__DetectObject_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DetectObject_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<DetectObject_Request>) -> bool;
}

// Corresponds to object_recognition_interfaces__srv__DetectObject_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DetectObject_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub structure_needs_at_least_one_member: u8,

}



impl Default for DetectObject_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !object_recognition_interfaces__srv__DetectObject_Request__init(&mut msg as *mut _) {
        panic!("Call to object_recognition_interfaces__srv__DetectObject_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DetectObject_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { object_recognition_interfaces__srv__DetectObject_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { object_recognition_interfaces__srv__DetectObject_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { object_recognition_interfaces__srv__DetectObject_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DetectObject_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DetectObject_Request where Self: Sized {
  const TYPE_NAME: &'static str = "object_recognition_interfaces/srv/DetectObject_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__object_recognition_interfaces__srv__DetectObject_Request() }
  }
}


#[link(name = "object_recognition_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__object_recognition_interfaces__srv__DetectObject_Response() -> *const std::ffi::c_void;
}

#[link(name = "object_recognition_interfaces__rosidl_generator_c")]
extern "C" {
    fn object_recognition_interfaces__srv__DetectObject_Response__init(msg: *mut DetectObject_Response) -> bool;
    fn object_recognition_interfaces__srv__DetectObject_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<DetectObject_Response>, size: usize) -> bool;
    fn object_recognition_interfaces__srv__DetectObject_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<DetectObject_Response>);
    fn object_recognition_interfaces__srv__DetectObject_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<DetectObject_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<DetectObject_Response>) -> bool;
}

// Corresponds to object_recognition_interfaces__srv__DetectObject_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DetectObject_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub object: rosidl_runtime_rs::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub confidence: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,

}



impl Default for DetectObject_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !object_recognition_interfaces__srv__DetectObject_Response__init(&mut msg as *mut _) {
        panic!("Call to object_recognition_interfaces__srv__DetectObject_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for DetectObject_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { object_recognition_interfaces__srv__DetectObject_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { object_recognition_interfaces__srv__DetectObject_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { object_recognition_interfaces__srv__DetectObject_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for DetectObject_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for DetectObject_Response where Self: Sized {
  const TYPE_NAME: &'static str = "object_recognition_interfaces/srv/DetectObject_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__object_recognition_interfaces__srv__DetectObject_Response() }
  }
}


#[link(name = "object_recognition_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__object_recognition_interfaces__srv__AddObject_Request() -> *const std::ffi::c_void;
}

#[link(name = "object_recognition_interfaces__rosidl_generator_c")]
extern "C" {
    fn object_recognition_interfaces__srv__AddObject_Request__init(msg: *mut AddObject_Request) -> bool;
    fn object_recognition_interfaces__srv__AddObject_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<AddObject_Request>, size: usize) -> bool;
    fn object_recognition_interfaces__srv__AddObject_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<AddObject_Request>);
    fn object_recognition_interfaces__srv__AddObject_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<AddObject_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<AddObject_Request>) -> bool;
}

// Corresponds to object_recognition_interfaces__srv__AddObject_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct AddObject_Request {

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



impl Default for AddObject_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !object_recognition_interfaces__srv__AddObject_Request__init(&mut msg as *mut _) {
        panic!("Call to object_recognition_interfaces__srv__AddObject_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for AddObject_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { object_recognition_interfaces__srv__AddObject_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { object_recognition_interfaces__srv__AddObject_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { object_recognition_interfaces__srv__AddObject_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for AddObject_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for AddObject_Request where Self: Sized {
  const TYPE_NAME: &'static str = "object_recognition_interfaces/srv/AddObject_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__object_recognition_interfaces__srv__AddObject_Request() }
  }
}


#[link(name = "object_recognition_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__object_recognition_interfaces__srv__AddObject_Response() -> *const std::ffi::c_void;
}

#[link(name = "object_recognition_interfaces__rosidl_generator_c")]
extern "C" {
    fn object_recognition_interfaces__srv__AddObject_Response__init(msg: *mut AddObject_Response) -> bool;
    fn object_recognition_interfaces__srv__AddObject_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<AddObject_Response>, size: usize) -> bool;
    fn object_recognition_interfaces__srv__AddObject_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<AddObject_Response>);
    fn object_recognition_interfaces__srv__AddObject_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<AddObject_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<AddObject_Response>) -> bool;
}

// Corresponds to object_recognition_interfaces__srv__AddObject_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct AddObject_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub message: rosidl_runtime_rs::String,

}



impl Default for AddObject_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !object_recognition_interfaces__srv__AddObject_Response__init(&mut msg as *mut _) {
        panic!("Call to object_recognition_interfaces__srv__AddObject_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for AddObject_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { object_recognition_interfaces__srv__AddObject_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { object_recognition_interfaces__srv__AddObject_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { object_recognition_interfaces__srv__AddObject_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for AddObject_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for AddObject_Response where Self: Sized {
  const TYPE_NAME: &'static str = "object_recognition_interfaces/srv/AddObject_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__object_recognition_interfaces__srv__AddObject_Response() }
  }
}






#[link(name = "object_recognition_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__object_recognition_interfaces__srv__DetectObject() -> *const std::ffi::c_void;
}

// Corresponds to object_recognition_interfaces__srv__DetectObject
#[allow(missing_docs, non_camel_case_types)]
pub struct DetectObject;

impl rosidl_runtime_rs::Service for DetectObject {
    type Request = DetectObject_Request;
    type Response = DetectObject_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__object_recognition_interfaces__srv__DetectObject() }
    }
}




#[link(name = "object_recognition_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__object_recognition_interfaces__srv__AddObject() -> *const std::ffi::c_void;
}

// Corresponds to object_recognition_interfaces__srv__AddObject
#[allow(missing_docs, non_camel_case_types)]
pub struct AddObject;

impl rosidl_runtime_rs::Service for AddObject {
    type Request = AddObject_Request;
    type Response = AddObject_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__object_recognition_interfaces__srv__AddObject() }
    }
}



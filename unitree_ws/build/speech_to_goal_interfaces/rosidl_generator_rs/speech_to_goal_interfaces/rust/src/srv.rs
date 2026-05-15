#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};




// Corresponds to speech_to_goal_interfaces__srv__LLMQuery_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct LLMQuery_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub query: std::string::String,

}



impl Default for LLMQuery_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::LLMQuery_Request::default())
  }
}

impl rosidl_runtime_rs::Message for LLMQuery_Request {
  type RmwMsg = super::srv::rmw::LLMQuery_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        query: msg.query.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        query: msg.query.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      query: msg.query.to_string(),
    }
  }
}


// Corresponds to speech_to_goal_interfaces__srv__LLMQuery_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct LLMQuery_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub waypoints: Vec<super::msg::Waypoint>,


    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub message: std::string::String,

}



impl Default for LLMQuery_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::LLMQuery_Response::default())
  }
}

impl rosidl_runtime_rs::Message for LLMQuery_Response {
  type RmwMsg = super::srv::rmw::LLMQuery_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        waypoints: msg.waypoints
          .into_iter()
          .map(|elem| super::msg::Waypoint::into_rmw_message(std::borrow::Cow::Owned(elem)).into_owned())
          .collect(),
        success: msg.success,
        message: msg.message.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        waypoints: msg.waypoints
          .iter()
          .map(|elem| super::msg::Waypoint::into_rmw_message(std::borrow::Cow::Borrowed(elem)).into_owned())
          .collect(),
      success: msg.success,
        message: msg.message.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      waypoints: msg.waypoints
          .into_iter()
          .map(super::msg::Waypoint::from_rmw_message)
          .collect(),
      success: msg.success,
      message: msg.message.to_string(),
    }
  }
}


// Corresponds to speech_to_goal_interfaces__srv__DetectIntent_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DetectIntent_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub text: std::string::String,

}



impl Default for DetectIntent_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::DetectIntent_Request::default())
  }
}

impl rosidl_runtime_rs::Message for DetectIntent_Request {
  type RmwMsg = super::srv::rmw::DetectIntent_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        text: msg.text.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        text: msg.text.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      text: msg.text.to_string(),
    }
  }
}


// Corresponds to speech_to_goal_interfaces__srv__DetectIntent_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct DetectIntent_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub intent: std::string::String,

}



impl Default for DetectIntent_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::DetectIntent_Response::default())
  }
}

impl rosidl_runtime_rs::Message for DetectIntent_Response {
  type RmwMsg = super::srv::rmw::DetectIntent_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        intent: msg.intent.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        intent: msg.intent.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      intent: msg.intent.to_string(),
    }
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



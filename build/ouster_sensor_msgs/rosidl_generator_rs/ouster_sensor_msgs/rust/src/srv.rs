#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};




// Corresponds to ouster_sensor_msgs__srv__GetConfig_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetConfig_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub structure_needs_at_least_one_member: u8,

}



impl Default for GetConfig_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::GetConfig_Request::default())
  }
}

impl rosidl_runtime_rs::Message for GetConfig_Request {
  type RmwMsg = super::srv::rmw::GetConfig_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        structure_needs_at_least_one_member: msg.structure_needs_at_least_one_member,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      structure_needs_at_least_one_member: msg.structure_needs_at_least_one_member,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      structure_needs_at_least_one_member: msg.structure_needs_at_least_one_member,
    }
  }
}


// Corresponds to ouster_sensor_msgs__srv__GetConfig_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetConfig_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub config: std::string::String,

}



impl Default for GetConfig_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::GetConfig_Response::default())
  }
}

impl rosidl_runtime_rs::Message for GetConfig_Response {
  type RmwMsg = super::srv::rmw::GetConfig_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        config: msg.config.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        config: msg.config.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      config: msg.config.to_string(),
    }
  }
}


// Corresponds to ouster_sensor_msgs__srv__SetConfig_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SetConfig_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub config_file: std::string::String,

}



impl Default for SetConfig_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::SetConfig_Request::default())
  }
}

impl rosidl_runtime_rs::Message for SetConfig_Request {
  type RmwMsg = super::srv::rmw::SetConfig_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        config_file: msg.config_file.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        config_file: msg.config_file.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      config_file: msg.config_file.to_string(),
    }
  }
}


// Corresponds to ouster_sensor_msgs__srv__SetConfig_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SetConfig_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub config: std::string::String,

}



impl Default for SetConfig_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::SetConfig_Response::default())
  }
}

impl rosidl_runtime_rs::Message for SetConfig_Response {
  type RmwMsg = super::srv::rmw::SetConfig_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        config: msg.config.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        config: msg.config.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      config: msg.config.to_string(),
    }
  }
}


// Corresponds to ouster_sensor_msgs__srv__GetMetadata_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetMetadata_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub structure_needs_at_least_one_member: u8,

}



impl Default for GetMetadata_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::GetMetadata_Request::default())
  }
}

impl rosidl_runtime_rs::Message for GetMetadata_Request {
  type RmwMsg = super::srv::rmw::GetMetadata_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        structure_needs_at_least_one_member: msg.structure_needs_at_least_one_member,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      structure_needs_at_least_one_member: msg.structure_needs_at_least_one_member,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      structure_needs_at_least_one_member: msg.structure_needs_at_least_one_member,
    }
  }
}


// Corresponds to ouster_sensor_msgs__srv__GetMetadata_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetMetadata_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub metadata: std::string::String,

}



impl Default for GetMetadata_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::GetMetadata_Response::default())
  }
}

impl rosidl_runtime_rs::Message for GetMetadata_Response {
  type RmwMsg = super::srv::rmw::GetMetadata_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        metadata: msg.metadata.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        metadata: msg.metadata.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      metadata: msg.metadata.to_string(),
    }
  }
}






#[link(name = "ouster_sensor_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__ouster_sensor_msgs__srv__GetConfig() -> *const std::ffi::c_void;
}

// Corresponds to ouster_sensor_msgs__srv__GetConfig
#[allow(missing_docs, non_camel_case_types)]
pub struct GetConfig;

impl rosidl_runtime_rs::Service for GetConfig {
    type Request = GetConfig_Request;
    type Response = GetConfig_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__ouster_sensor_msgs__srv__GetConfig() }
    }
}




#[link(name = "ouster_sensor_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__ouster_sensor_msgs__srv__SetConfig() -> *const std::ffi::c_void;
}

// Corresponds to ouster_sensor_msgs__srv__SetConfig
#[allow(missing_docs, non_camel_case_types)]
pub struct SetConfig;

impl rosidl_runtime_rs::Service for SetConfig {
    type Request = SetConfig_Request;
    type Response = SetConfig_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__ouster_sensor_msgs__srv__SetConfig() }
    }
}




#[link(name = "ouster_sensor_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__ouster_sensor_msgs__srv__GetMetadata() -> *const std::ffi::c_void;
}

// Corresponds to ouster_sensor_msgs__srv__GetMetadata
#[allow(missing_docs, non_camel_case_types)]
pub struct GetMetadata;

impl rosidl_runtime_rs::Service for GetMetadata {
    type Request = GetMetadata_Request;
    type Response = GetMetadata_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__ouster_sensor_msgs__srv__GetMetadata() }
    }
}



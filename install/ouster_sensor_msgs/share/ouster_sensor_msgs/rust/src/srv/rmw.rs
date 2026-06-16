#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



#[link(name = "ouster_sensor_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__ouster_sensor_msgs__srv__GetConfig_Request() -> *const std::ffi::c_void;
}

#[link(name = "ouster_sensor_msgs__rosidl_generator_c")]
extern "C" {
    fn ouster_sensor_msgs__srv__GetConfig_Request__init(msg: *mut GetConfig_Request) -> bool;
    fn ouster_sensor_msgs__srv__GetConfig_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<GetConfig_Request>, size: usize) -> bool;
    fn ouster_sensor_msgs__srv__GetConfig_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<GetConfig_Request>);
    fn ouster_sensor_msgs__srv__GetConfig_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<GetConfig_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<GetConfig_Request>) -> bool;
}

// Corresponds to ouster_sensor_msgs__srv__GetConfig_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetConfig_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub structure_needs_at_least_one_member: u8,

}



impl Default for GetConfig_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !ouster_sensor_msgs__srv__GetConfig_Request__init(&mut msg as *mut _) {
        panic!("Call to ouster_sensor_msgs__srv__GetConfig_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for GetConfig_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__srv__GetConfig_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__srv__GetConfig_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__srv__GetConfig_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for GetConfig_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for GetConfig_Request where Self: Sized {
  const TYPE_NAME: &'static str = "ouster_sensor_msgs/srv/GetConfig_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__ouster_sensor_msgs__srv__GetConfig_Request() }
  }
}


#[link(name = "ouster_sensor_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__ouster_sensor_msgs__srv__GetConfig_Response() -> *const std::ffi::c_void;
}

#[link(name = "ouster_sensor_msgs__rosidl_generator_c")]
extern "C" {
    fn ouster_sensor_msgs__srv__GetConfig_Response__init(msg: *mut GetConfig_Response) -> bool;
    fn ouster_sensor_msgs__srv__GetConfig_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<GetConfig_Response>, size: usize) -> bool;
    fn ouster_sensor_msgs__srv__GetConfig_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<GetConfig_Response>);
    fn ouster_sensor_msgs__srv__GetConfig_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<GetConfig_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<GetConfig_Response>) -> bool;
}

// Corresponds to ouster_sensor_msgs__srv__GetConfig_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetConfig_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub config: rosidl_runtime_rs::String,

}



impl Default for GetConfig_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !ouster_sensor_msgs__srv__GetConfig_Response__init(&mut msg as *mut _) {
        panic!("Call to ouster_sensor_msgs__srv__GetConfig_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for GetConfig_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__srv__GetConfig_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__srv__GetConfig_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__srv__GetConfig_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for GetConfig_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for GetConfig_Response where Self: Sized {
  const TYPE_NAME: &'static str = "ouster_sensor_msgs/srv/GetConfig_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__ouster_sensor_msgs__srv__GetConfig_Response() }
  }
}


#[link(name = "ouster_sensor_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__ouster_sensor_msgs__srv__SetConfig_Request() -> *const std::ffi::c_void;
}

#[link(name = "ouster_sensor_msgs__rosidl_generator_c")]
extern "C" {
    fn ouster_sensor_msgs__srv__SetConfig_Request__init(msg: *mut SetConfig_Request) -> bool;
    fn ouster_sensor_msgs__srv__SetConfig_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<SetConfig_Request>, size: usize) -> bool;
    fn ouster_sensor_msgs__srv__SetConfig_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<SetConfig_Request>);
    fn ouster_sensor_msgs__srv__SetConfig_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<SetConfig_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<SetConfig_Request>) -> bool;
}

// Corresponds to ouster_sensor_msgs__srv__SetConfig_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SetConfig_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub config_file: rosidl_runtime_rs::String,

}



impl Default for SetConfig_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !ouster_sensor_msgs__srv__SetConfig_Request__init(&mut msg as *mut _) {
        panic!("Call to ouster_sensor_msgs__srv__SetConfig_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for SetConfig_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__srv__SetConfig_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__srv__SetConfig_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__srv__SetConfig_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for SetConfig_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for SetConfig_Request where Self: Sized {
  const TYPE_NAME: &'static str = "ouster_sensor_msgs/srv/SetConfig_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__ouster_sensor_msgs__srv__SetConfig_Request() }
  }
}


#[link(name = "ouster_sensor_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__ouster_sensor_msgs__srv__SetConfig_Response() -> *const std::ffi::c_void;
}

#[link(name = "ouster_sensor_msgs__rosidl_generator_c")]
extern "C" {
    fn ouster_sensor_msgs__srv__SetConfig_Response__init(msg: *mut SetConfig_Response) -> bool;
    fn ouster_sensor_msgs__srv__SetConfig_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<SetConfig_Response>, size: usize) -> bool;
    fn ouster_sensor_msgs__srv__SetConfig_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<SetConfig_Response>);
    fn ouster_sensor_msgs__srv__SetConfig_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<SetConfig_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<SetConfig_Response>) -> bool;
}

// Corresponds to ouster_sensor_msgs__srv__SetConfig_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SetConfig_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub config: rosidl_runtime_rs::String,

}



impl Default for SetConfig_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !ouster_sensor_msgs__srv__SetConfig_Response__init(&mut msg as *mut _) {
        panic!("Call to ouster_sensor_msgs__srv__SetConfig_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for SetConfig_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__srv__SetConfig_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__srv__SetConfig_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__srv__SetConfig_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for SetConfig_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for SetConfig_Response where Self: Sized {
  const TYPE_NAME: &'static str = "ouster_sensor_msgs/srv/SetConfig_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__ouster_sensor_msgs__srv__SetConfig_Response() }
  }
}


#[link(name = "ouster_sensor_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__ouster_sensor_msgs__srv__GetMetadata_Request() -> *const std::ffi::c_void;
}

#[link(name = "ouster_sensor_msgs__rosidl_generator_c")]
extern "C" {
    fn ouster_sensor_msgs__srv__GetMetadata_Request__init(msg: *mut GetMetadata_Request) -> bool;
    fn ouster_sensor_msgs__srv__GetMetadata_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<GetMetadata_Request>, size: usize) -> bool;
    fn ouster_sensor_msgs__srv__GetMetadata_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<GetMetadata_Request>);
    fn ouster_sensor_msgs__srv__GetMetadata_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<GetMetadata_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<GetMetadata_Request>) -> bool;
}

// Corresponds to ouster_sensor_msgs__srv__GetMetadata_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetMetadata_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub structure_needs_at_least_one_member: u8,

}



impl Default for GetMetadata_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !ouster_sensor_msgs__srv__GetMetadata_Request__init(&mut msg as *mut _) {
        panic!("Call to ouster_sensor_msgs__srv__GetMetadata_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for GetMetadata_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__srv__GetMetadata_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__srv__GetMetadata_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__srv__GetMetadata_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for GetMetadata_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for GetMetadata_Request where Self: Sized {
  const TYPE_NAME: &'static str = "ouster_sensor_msgs/srv/GetMetadata_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__ouster_sensor_msgs__srv__GetMetadata_Request() }
  }
}


#[link(name = "ouster_sensor_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__ouster_sensor_msgs__srv__GetMetadata_Response() -> *const std::ffi::c_void;
}

#[link(name = "ouster_sensor_msgs__rosidl_generator_c")]
extern "C" {
    fn ouster_sensor_msgs__srv__GetMetadata_Response__init(msg: *mut GetMetadata_Response) -> bool;
    fn ouster_sensor_msgs__srv__GetMetadata_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<GetMetadata_Response>, size: usize) -> bool;
    fn ouster_sensor_msgs__srv__GetMetadata_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<GetMetadata_Response>);
    fn ouster_sensor_msgs__srv__GetMetadata_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<GetMetadata_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<GetMetadata_Response>) -> bool;
}

// Corresponds to ouster_sensor_msgs__srv__GetMetadata_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetMetadata_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub metadata: rosidl_runtime_rs::String,

}



impl Default for GetMetadata_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !ouster_sensor_msgs__srv__GetMetadata_Response__init(&mut msg as *mut _) {
        panic!("Call to ouster_sensor_msgs__srv__GetMetadata_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for GetMetadata_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__srv__GetMetadata_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__srv__GetMetadata_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__srv__GetMetadata_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for GetMetadata_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for GetMetadata_Response where Self: Sized {
  const TYPE_NAME: &'static str = "ouster_sensor_msgs/srv/GetMetadata_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__ouster_sensor_msgs__srv__GetMetadata_Response() }
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



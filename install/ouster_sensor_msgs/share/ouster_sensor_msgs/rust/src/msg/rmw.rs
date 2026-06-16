#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "ouster_sensor_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__ouster_sensor_msgs__msg__PacketMsg() -> *const std::ffi::c_void;
}

#[link(name = "ouster_sensor_msgs__rosidl_generator_c")]
extern "C" {
    fn ouster_sensor_msgs__msg__PacketMsg__init(msg: *mut PacketMsg) -> bool;
    fn ouster_sensor_msgs__msg__PacketMsg__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<PacketMsg>, size: usize) -> bool;
    fn ouster_sensor_msgs__msg__PacketMsg__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<PacketMsg>);
    fn ouster_sensor_msgs__msg__PacketMsg__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<PacketMsg>, out_seq: *mut rosidl_runtime_rs::Sequence<PacketMsg>) -> bool;
}

// Corresponds to ouster_sensor_msgs__msg__PacketMsg
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct PacketMsg {

    // This member is not documented.
    #[allow(missing_docs)]
    pub buf: rosidl_runtime_rs::Sequence<u8>,

}



impl Default for PacketMsg {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !ouster_sensor_msgs__msg__PacketMsg__init(&mut msg as *mut _) {
        panic!("Call to ouster_sensor_msgs__msg__PacketMsg__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for PacketMsg {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__msg__PacketMsg__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__msg__PacketMsg__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__msg__PacketMsg__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for PacketMsg {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for PacketMsg where Self: Sized {
  const TYPE_NAME: &'static str = "ouster_sensor_msgs/msg/PacketMsg";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__ouster_sensor_msgs__msg__PacketMsg() }
  }
}


#[link(name = "ouster_sensor_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__ouster_sensor_msgs__msg__Telemetry() -> *const std::ffi::c_void;
}

#[link(name = "ouster_sensor_msgs__rosidl_generator_c")]
extern "C" {
    fn ouster_sensor_msgs__msg__Telemetry__init(msg: *mut Telemetry) -> bool;
    fn ouster_sensor_msgs__msg__Telemetry__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Telemetry>, size: usize) -> bool;
    fn ouster_sensor_msgs__msg__Telemetry__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Telemetry>);
    fn ouster_sensor_msgs__msg__Telemetry__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Telemetry>, out_seq: *mut rosidl_runtime_rs::Sequence<Telemetry>) -> bool;
}

// Corresponds to ouster_sensor_msgs__msg__Telemetry
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]

/// This message defines the telemetry data for Ouster sensors.

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Telemetry {
    /// Message header
    pub header: std_msgs::msg::rmw::Header,

    /// Telemetry fields for more information on these fields and their meaning, please review:
    /// https://static.ouster.dev/sensor-docs/image_route1/image_route2/thermal_int_guide/therm_int_guide.html
    /// the thermal shutdown countdown.
    pub countdown_thermal_shutdown: u16,

    /// the shot limiting countdown.
    pub countdown_shot_limiting: u16,

    /// the thermal shutdown status. 0 = NORMAL, 1 = SHUTDOWN IMMINENT.
    pub thermal_shutdown: u8,

    /// the shot limiting status. 0 = NORMAL OPERATION.
    pub shot_limiting: u8,

}

impl Telemetry {
    /// ThermalShutdownStatus thermal_shutdown
    /// Normal operation
    pub const THERMAL_SHUTDOWN_NORMAL: u8 = 0;

    /// Thermal Shutdown imminent
    pub const THERMAL_SHUTDOWN_IMMINENT: u8 = 1;

    /// ShotLimitingStatus shot_limiting
    /// Normal operation
    pub const SHOT_LIMITING_NORMAL: u8 = 0;

    /// Shot limiting imminent
    pub const SHOT_LIMITING_IMMINENT: u8 = 1;

    /// Shot limiting reduction by 0 to 10%
    pub const SHOT_LIMITING_REDUCTION_0_10: u8 = 2;

    /// Shot limiting reduction by 10 to 20%
    pub const SHOT_LIMITING_REDUCTION_10_20: u8 = 3;

    /// Shot limiting reduction by 20 to 30%
    pub const SHOT_LIMITING_REDUCTION_20_30: u8 = 4;

    /// Shot limiting reduction by 30 to 40%
    pub const SHOT_LIMITING_REDUCTION_30_40: u8 = 5;

    /// Shot limiting reduction by 40 to 50%
    pub const SHOT_LIMITING_REDUCTION_40_50: u8 = 6;

    /// Shot limiting reduction by 50 to 60%
    pub const SHOT_LIMITING_REDUCTION_50_60: u8 = 7;

    /// Shot limiting reduction by 60 to 70%
    pub const SHOT_LIMITING_REDUCTION_60_70: u8 = 8;

    /// Shot limiting reduction by 70 to 80%
    pub const SHOT_LIMITING_REDUCTION_70_75: u8 = 9;

}


impl Default for Telemetry {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !ouster_sensor_msgs__msg__Telemetry__init(&mut msg as *mut _) {
        panic!("Call to ouster_sensor_msgs__msg__Telemetry__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Telemetry {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__msg__Telemetry__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__msg__Telemetry__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ouster_sensor_msgs__msg__Telemetry__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Telemetry {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Telemetry where Self: Sized {
  const TYPE_NAME: &'static str = "ouster_sensor_msgs/msg/Telemetry";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__ouster_sensor_msgs__msg__Telemetry() }
  }
}



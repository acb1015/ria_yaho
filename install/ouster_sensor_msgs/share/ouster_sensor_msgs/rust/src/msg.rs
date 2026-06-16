#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to ouster_sensor_msgs__msg__PacketMsg

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct PacketMsg {

    // This member is not documented.
    #[allow(missing_docs)]
    pub buf: Vec<u8>,

}



impl Default for PacketMsg {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::PacketMsg::default())
  }
}

impl rosidl_runtime_rs::Message for PacketMsg {
  type RmwMsg = super::msg::rmw::PacketMsg;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        buf: msg.buf.into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        buf: msg.buf.as_slice().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      buf: msg.buf
          .into_iter()
          .collect(),
    }
  }
}


// Corresponds to ouster_sensor_msgs__msg__Telemetry
/// This message defines the telemetry data for Ouster sensors.

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Telemetry {
    /// Message header
    pub header: std_msgs::msg::Header,

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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::Telemetry::default())
  }
}

impl rosidl_runtime_rs::Message for Telemetry {
  type RmwMsg = super::msg::rmw::Telemetry;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        countdown_thermal_shutdown: msg.countdown_thermal_shutdown,
        countdown_shot_limiting: msg.countdown_shot_limiting,
        thermal_shutdown: msg.thermal_shutdown,
        shot_limiting: msg.shot_limiting,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
      countdown_thermal_shutdown: msg.countdown_thermal_shutdown,
      countdown_shot_limiting: msg.countdown_shot_limiting,
      thermal_shutdown: msg.thermal_shutdown,
      shot_limiting: msg.shot_limiting,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      countdown_thermal_shutdown: msg.countdown_thermal_shutdown,
      countdown_shot_limiting: msg.countdown_shot_limiting,
      thermal_shutdown: msg.thermal_shutdown,
      shot_limiting: msg.shot_limiting,
    }
  }
}



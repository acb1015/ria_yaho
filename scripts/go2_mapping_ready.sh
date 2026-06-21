#!/usr/bin/env bash
set -euo pipefail

WS="${GO2_WS:-$HOME/go2_ws}"
SENSOR_IP="${OUSTER_SENSOR_IP:-169.254.6.117}"
HOST_IFACE="${OUSTER_HOST_IFACE:-enx00e099010d5f}"
HOST_IP="${OUSTER_HOST_IP:-169.254.0.2}"
RVIZ="${RVIZ:-false}"

say() {
  printf '[go2-mapping] %s\n' "$*"
}

fail() {
  printf '[go2-mapping] ERROR: %s\n' "$*" >&2
  exit 1
}

require_file() {
  [[ -f "$1" ]] || fail "missing file: $1"
}

check_interface() {
  say "checking ${HOST_IFACE} (${HOST_IP})"
  ip link show "$HOST_IFACE" >/dev/null 2>&1 || fail "network interface ${HOST_IFACE} not found"
  ip addr show "$HOST_IFACE" | grep -q "${HOST_IP}/" || fail "${HOST_IFACE} does not have ${HOST_IP}"
  ip link show "$HOST_IFACE" | grep -q "LOWER_UP" || fail "${HOST_IFACE} link is not physically up"
}

check_udp_buffers() {
  local max default
  max="$(sysctl -n net.core.rmem_max)"
  default="$(sysctl -n net.core.rmem_default)"
  say "UDP receive buffers: rmem_max=${max}, rmem_default=${default}"
  [[ "$max" -ge 8388608 ]] || fail "net.core.rmem_max is too small; run: sudo sysctl -w net.core.rmem_max=8388608"
  [[ "$default" -ge 8388608 ]] || fail "net.core.rmem_default is too small; run: sudo sysctl -w net.core.rmem_default=8388608"
}

check_config() {
  local driver_src="$WS/src/ouster-ros/ouster-ros/config/driver_params.yaml"
  local driver_install="$WS/install/ouster_ros/share/ouster_ros/config/driver_params.yaml"
  local fastlio_src="$WS/src/FAST_LIO/config/ouster64.yaml"
  local fastlio_install="$WS/install/fast_lio/share/fast_lio/config/ouster64.yaml"

  require_file "$driver_src"
  require_file "$driver_install"
  require_file "$fastlio_src"
  require_file "$fastlio_install"

  cmp -s "$driver_src" "$driver_install" || fail "driver_params.yaml differs between src and install"
  cmp -s "$fastlio_src" "$fastlio_install" || fail "ouster64.yaml differs between src and install"

  grep -q "lidar_mode: '1024x20'" "$driver_install" || fail "driver lidar_mode is not 1024x20"
  grep -q "timestamp_mode: 'TIME_FROM_INTERNAL_OSC'" "$driver_install" || fail "timestamp_mode must remain TIME_FROM_INTERNAL_OSC"
  grep -q "point_cloud_frame: os_sensor" "$driver_install" || fail "point_cloud_frame must remain os_sensor"
  grep -q "use_system_default_qos: true" "$driver_install" || fail "use_system_default_qos must remain true"
  grep -q "scan_rate: 20" "$fastlio_install" || fail "FAST-LIO scan_rate is not 20"

  say "config is synced and set for 1024x20"
}

wait_for_lidar() {
  say "waiting for Ouster OS1 at ${SENSOR_IP}"
  for attempt in $(seq 1 30); do
    if ping -c1 -W1 "$SENSOR_IP" >/dev/null 2>&1; then
      if curl -m 3 -fs "http://${SENSOR_IP}/api/v1/sensor/metadata/sensor_info" >/dev/null; then
        say "Ouster HTTP metadata API is responding"
        return 0
      fi
      say "ping ok, HTTP not ready yet (${attempt}/30)"
    else
      say "no ping response yet (${attempt}/30)"
    fi
    sleep 2
  done

  ip neigh show "$SENSOR_IP" dev "$HOST_IFACE" || true
  fail "lidar is not reachable; power-cycle OS1 for 5-10 seconds, then wait about 1 minute"
}

launch_mapping() {
  source /opt/ros/humble/setup.bash
  source "$WS/install/setup.bash"
  say "launching mapping with rviz:=${RVIZ}"
  exec ros2 launch "$WS/go2_mapping.launch.py" "rviz:=${RVIZ}"
}

check_interface
check_udp_buffers
check_config
wait_for_lidar
launch_mapping

#!/usr/bin/env python3
"""
calibrate_imu_manual.py
-----------------------
Go2 L1 라이다 IMU 캘리브레이션 값을 계산해서 ~/Desktop/imu_calib_data.yaml 로 저장합니다.
원본 calibrate_imu(C++)와 '동일한 수식'을 쓰되, 로봇을 자동으로 회전시키지 않고
사용자가 직접 (1) 가만히 세우고 (2) 손/리모컨으로 제자리 회전시키면 됩니다.

전제: 로봇이 평평한 바닥에 '기립(standing)' 상태. unitree_setup.sh 를 source 해서
      /utlidar/imu 가 들어오는 상태여야 함.

실행:
    cd ~/go2_ws && source unitree_setup.sh && source install/setup.bash
    python3 calibrate_imu_manual.py
"""
import math, time, os, shutil, datetime
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu

THETA = 15.1 / 180.0 * math.pi   # 원본과 동일: IMU 를 z-up 으로 맞추는 기울기 보정각
GRAVITY = 9.81

STATIC_SETTLE = 3.0   # 정지 안정화(수집 안 함)
STATIC_SECS   = 12.0  # 정지 데이터 수집
ROT_SETTLE    = 4.0   # 회전 시작 안정화(수집 안 함)
ROT_SECS      = 20.0  # 회전 데이터 수집


def preprocess(imu):
    """원본 imu_handler 와 동일한 전처리 (부호변환 + theta 회전)."""
    x = imu.angular_velocity.x
    y = -imu.angular_velocity.y
    z = -imu.angular_velocity.z
    gx = x * math.cos(THETA) - z * math.sin(THETA)
    gy = y
    gz = x * math.sin(THETA) + z * math.cos(THETA)

    ax_ = imu.linear_acceleration.x
    ay_ = -imu.linear_acceleration.y
    az_ = -imu.linear_acceleration.z
    ax = ax_ * math.cos(THETA) - az_ * math.sin(THETA)
    ay = ay_
    az = ax_ * math.sin(THETA) + az_ * math.cos(THETA)
    return (gx, gy, gz, ax, ay, az)   # gyro xyz, acc xyz (전처리 후)


class Calib(Node):
    def __init__(self):
        super().__init__('calibrate_imu_manual')
        self.latest = None
        self.count = 0
        self.create_subscription(Imu, '/utlidar/imu', self.cb, 300)

    def cb(self, m):
        self.latest = preprocess(m)
        self.count += 1


def collect(node, settle, secs, label, show_rot=False):
    """settle 초 대기(수집X) 후 secs 초 동안 수집."""
    # settle
    t0 = time.time()
    while time.time() - t0 < settle:
        rclpy.spin_once(node, timeout_sec=0.02)
    # collect
    data = []
    t0 = time.time()
    last = -1
    while time.time() - t0 < secs:
        rclpy.spin_once(node, timeout_sec=0.02)
        if node.latest is not None:
            data.append(node.latest)
        el = time.time() - t0
        if int(el) != last:
            last = int(el)
            gz = node.latest[2] if node.latest else 0.0
            extra = f"  gyroZ={gz:+.2f} rad/s" if show_rot else ""
            print(f"   [{label}] {secs - el:4.0f}s 남음 | 샘플 {len(data):5d}{extra}")
    return np.array(data) if data else np.empty((0, 6))


def main():
    rclpy.init()
    node = Calib()

    print("=" * 60)
    print(" Go2 IMU 수동 캘리브레이션")
    print("=" * 60)
    print(" /utlidar/imu 수신 확인 중...")
    t0 = time.time()
    while node.latest is None and time.time() - t0 < 5:
        rclpy.spin_once(node, timeout_sec=0.1)
    if node.latest is None:
        print(" !! /utlidar/imu 가 안 들어옵니다. unitree_setup.sh source 했는지,")
        print("    Go2 가 켜져있는지 확인하세요.")
        rclpy.shutdown(); return
    print(f" OK (수신 중, {node.count} 샘플)\n")

    # ---------- 1) 정지 ----------
    input(">> [1단계] 로봇을 평평한 곳에 '가만히 기립' 시키고 Enter (이후 12초간 움직이지 마세요): ")
    static = collect(node, STATIC_SETTLE, STATIC_SECS, "정지")
    if len(static) < 50:
        print(" !! 정지 샘플이 너무 적습니다."); rclpy.shutdown(); return

    acc_bias_x = static[:, 3].mean()
    acc_bias_y = static[:, 4].mean()
    acc_bias_z = static[:, 5].mean() - GRAVITY   # 중력 제거
    ang_bias_x = static[:, 0].mean()
    ang_bias_y = static[:, 1].mean()
    ang_bias_z = static[:, 2].mean()
    print(f"\n   정지 결과: acc_bias=({acc_bias_x:+.4f},{acc_bias_y:+.4f},{acc_bias_z:+.4f})"
          f"  ang_bias=({ang_bias_x:+.5f},{ang_bias_y:+.5f},{ang_bias_z:+.5f})\n")

    # ---------- 2) 회전 ----------
    print(">> [2단계] 이제 로봇을 '제자리에서 한 방향으로 꾸준히' 회전시키세요")
    print("   (왼쪽=반시계 권장, ~80도/초 정도. 방향은 결과에 영향 없음)")
    input("   회전을 시작한 뒤 Enter (이후 20초간 계속 회전): ")
    rot = collect(node, ROT_SETTLE, ROT_SECS, "회전", show_rot=True)
    if len(rot) < 50:
        print(" !! 회전 샘플이 너무 적습니다."); rclpy.shutdown(); return

    ang_rot_x = rot[:, 0].mean() - ang_bias_x
    ang_rot_y = rot[:, 1].mean() - ang_bias_y
    ang_rot_z = rot[:, 2].mean() - ang_bias_z
    print(f"\n   회전 평균 gyroZ = {ang_rot_z:+.3f} rad/s ({math.degrees(ang_rot_z):+.0f} deg/s)")
    if abs(ang_rot_z) < 0.3:
        print("   !! 경고: z축 회전이 너무 약합니다(>0.5rad/s 권장). 더 빠르게 다시 하세요.")
    ang_z2x_proj = -ang_rot_x / ang_rot_z
    ang_z2y_proj = -ang_rot_y / ang_rot_z

    # ---------- 저장 ----------
    home = os.path.expanduser('~')
    out = os.path.join(home, 'Desktop', 'imu_calib_data.yaml')
    if os.path.exists(out):
        bak = out + '.bak_' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        shutil.copy(out, bak)
        print(f"\n   기존 파일 백업: {bak}")

    vals = {
        'acc_bias_x': acc_bias_x, 'acc_bias_y': acc_bias_y, 'acc_bias_z': acc_bias_z,
        'ang_bias_x': ang_bias_x, 'ang_bias_y': ang_bias_y, 'ang_bias_z': ang_bias_z,
        'ang_z2x_proj': ang_z2x_proj, 'ang_z2y_proj': ang_z2y_proj,
    }
    with open(out, 'w') as f:
        for k in ['acc_bias_x', 'acc_bias_y', 'acc_bias_z',
                  'ang_bias_x', 'ang_bias_y', 'ang_bias_z',
                  'ang_z2x_proj', 'ang_z2y_proj']:
            f.write(f"{k}: {vals[k]:g}\n")

    print("\n" + "=" * 60)
    print(" 캘리브레이션 완료! 저장 위치:", out)
    print("=" * 60)
    for k in vals:
        print(f"   {k}: {vals[k]:.6f}")
    print("\n 시스템을 재시작하면 transform_everything 가 이 값을 자동 로드합니다.")
    rclpy.shutdown()


if __name__ == '__main__':
    main()

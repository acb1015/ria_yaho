# Agent Handoff — Go2 + Orin NX + Ouster OS1 SLAM 매핑

> 이 문서는 다른 AI 에이전트가 컨텍스트 없이 작업을 이어받기 위한 핸드오프 문서다.
> 최종 업데이트: 2026-06-16. 작성 환경: ROS2 Humble / Ubuntu 22.04 / Jetson Orin NX.

---

## 0. 한 줄 현황
실시간 LIO(FAST-LIO2) + PGO 루프클로저 파이프라인을 구축했고 핵심 발산 문제(시간 동기화)를 해결했다. **현재 라이다(Ouster OS1)가 하드웨어 응답 불능 상태(파워 사이클 필요)라 막혀 있다.** 2026-06-16 추가 확인에서도 ping/HTTP 모두 실패, ARP는 간헐적으로 MAC만 보이는 상태였다. 라이다 복구 후 "20Hz 모드로 빠른-회전 발산 개선" 테스트를 이어가면 된다.

---

## 1. 목표
- **최종**: Go2 4족로봇(Orin NX 탑재)에 Ouster OS1-64를 달아 실시간 LiDAR-Inertial SLAM으로 지도를 만들고, 추후 Nav2 자율주행으로 연결.
- **현재 단계 목표**: 사람이 Go2를 원격조종(리모컨/앱)으로 몰면서 실시간 매핑 → PGO 루프클로저로 맵 정합 → 맵 저장. (로봇 주행 명령은 ROS로 안 보냄. ROS 스택은 "센서 구동 + LIO + PGO"만 담당.)
- IMU는 **Ouster 내장 IMU(`/ouster/imu`)** 사용. Go2 몸통 IMU 아님. (Unitree 공식 SLAM도 라이다 내장 IMU를 쓴다는 것 확인함. 단, 추후 Go2 leg odometry를 EKF로 융합하는 안은 살아있음 — 9장 참고.)

---

## 2. 하드웨어 & 네트워크
| 구성 | 값 |
|---|---|
| 라이다 | Ouster OS1-64-U13-SR, FW 3.1.0, S/N 122619005017 |
| 라이다 IP | `169.254.6.117`, 호스트 측 전용 USB-이더넷 `enx00e099010d5f` = `169.254.0.2` |
| 라이다 udp_dest | `169.254.0.2` |
| Go2 통신 | CycloneDDS, 인터페이스 `eno1` (`192.168.123.1/24`) |
| 메타데이터 | `/home/ria4065/go2_ws/169.254.6-metadata.json` (IMU extrinsic 등 원본값 보유) |

> 라이다 IMU 메타데이터: `imu_to_sensor_transform` 회전=identity, translation=(-2.441, -9.725, 7.533)mm.
> `lidar_to_sensor_transform` 회전 = Z축 180° (`diag(-1,-1,1)`). **이 180° 차이가 과거 발산의 원인이었음 (6장 참고).**

---

## 3. 워크스페이스 구조 (`/home/ria4065/go2_ws/src/`)
| 패키지 | 역할 | 출처 |
|---|---|---|
| `ouster-ros` | OS1 드라이버 (`/ouster/points`, `/ouster/imu`) | 공식 |
| `unitree_ros2`, `unitree_sdk2` | Go2 DDS 통신 (현재는 모니터링용) | 공식 |
| `FAST_LIO` | LIO 오도메트리+맵 | Taeyoung96/FAST_LIO_ROS2 (Ouster 네이티브 지원, `config/ouster64.yaml`) |
| `livox_ros_driver2` | FAST_LIO의 빌드 의존성(코드 구조상 필수, Ouster만 써도 필요) | Livox |
| `interface` | PGO용 srv 메시지 정의 (Livox 의존 없음, `std_msgs`만) | liangheming/FASTLIO2_ROS2 |
| `pgo` | PGO 루프클로저 (GTSAM 기반 pose graph) | liangheming/FASTLIO2_ROS2 |
| `FAST_LIO_ROS2` | 클론 잔재(거의 빈 래퍼). 무시 가능 | — |
| `go2_motion_ws` | **이 작업과 무관(다른 작업). 건드리지 말 것** | — |

- Livox-SDK2: `~/Livox-SDK2`에서 빌드해서 `sudo make install` 완료 (`/usr/local/lib/liblivox_lidar_sdk_shared.so`).
- GTSAM: `ros-humble-gtsam` (apt) 설치됨.
- 통합 launch: **`/home/ria4065/go2_ws/go2_mapping.launch.py`** (driver→FAST-LIO→PGO 순차 기동).

---

## 4. 완료된 작업 (✅)
1. `unitree_ros2/setup.sh`,`setup_default.sh`: foxy→humble, `enp3s0`→`eno1` 수정.
2. Jetson 성능 MAXN 고정 (`nvpmodel -m 0`, `jetson_clocks`).
3. 커널 UDP 버퍼: `net.core.rmem_max=8388608`, `rmem_default=8388608` (sysctl, **재부팅 시 초기화됨 → 매 세션 재적용 필요**).
4. FAST_LIO 설치/빌드 (버그 6건 수정, 5장).
5. PGO 통합 (`interface`+`pgo` 빌드, 토픽 리매핑, NaN 가드 2개 추가).
6. 통합 launch 작성 (`go2_mapping.launch.py`).
7. **시간 동기화 해결**: `TIME_FROM_ROS_TIME` → `TIME_FROM_INTERNAL_OSC` (발산 주원인이었음).
8. **IMU 공분산 튜닝**: `acc_cov`/`gyr_cov` 0.5→0.1, `b_*_cov` 0.001→0.0001 (회전 드리프트 22m→1.3m로 개선).
9. 라이다-IMU extrinsic 반영 (`extrinsic_T`에 메타데이터 lever-arm).
10. 발산 디버깅용 rosbag 녹화: `/home/ria4065/go2_ws/bags/diverge_test` (122초, /ouster/points+imu). IMU 분석 스크립트: `/home/ria4065/go2_ws/bags/analyze_imu.py`.

---

## 5. 수정한 버그 (FAST_LIO 통합 시) — 되돌리지 말 것
1. 패키지를 `src/` 바로 아래로 재배치 (build.sh 상대경로 가정).
2. Livox-SDK2 시스템 설치.
3. `ouster64.yaml` 토픽명: `/os_cloud_node/*` → `/ouster/points`,`/ouster/imu`.
4. `extrinsic_R` 정수→실수 (`[1,0,0...]`→`[1.0,0.0,0.0...]`, 파라미터 타입 에러).
5. QoS: `use_system_default_qos: true` (드라이버 BEST_EFFORT ↔ FAST_LIO RELIABLE 불일치 해결).
6. `FAST_LIO/src/preprocess.h`의 `ouster_ros::Point` 구조체 `ring` 타입 `uint8_t`→`uint16_t` (실제 드라이버와 일치, `Failed to find match for field 'ring'` 해결). **소스 수정이므로 fast_lio 재빌드 필요했음.**

---

## 6. 발산(divergence) 디버깅 — 핵심 결론
"조금만 움직여도 로봇이 맵 밖으로 튀어나가며 SLAM 깨짐" 문제를 깊이 추적함.

- **연산은 병목 아님**: FAST-LIO 스캔당 처리시간 ~11ms (주기 100ms의 11%). 피처추출/다운샘플 불필요. (사용자가 "포인트 많아 느리다"고 의심했으나 측정상 아님. RViz에 많이 보이는 건 누적맵(시각화)이지 연산량 아님.)
- **IMU 데이터 자체는 정상**: 정지 시 accel_z≈9.8 m/s², gyro≈0. 단위(m/s², rad/s) 정상.
- **발산 원인 1 (해결됨) — 좌표계 180°**: `point_cloud_frame`이 `os_lidar`(sensor 대비 Z 180° 회전)였고 IMU(`os_imu`)는 identity인데 `extrinsic_R`=identity로 둬서 회전 시 즉시 발산. → **`point_cloud_frame: os_sensor`로 변경하여 해결.**
- **발산 원인 2 (해결됨) — 시간 동기화**: `TIME_FROM_ROS_TIME`은 패킷 수신시각 기반인데, CPU 부하(원격 데스크톱 스트리밍 `nxcodec.bin`/`nxnode.bin`가 CPU 70%+ 점유) 때문에 라이다/IMU 수신 지연이 들쭉날쭉 → dt 깨짐 → 직진에서도 즉시 발산. → **`TIME_FROM_INTERNAL_OSC`로 변경하여 해결.** (라이다 HW 시계가 라이다+IMU 둘 다 타임스탬프 → CPU 무관하게 dt 정확.)
- **발산 원인 3 (부분 해결) — IMU 공분산 과대**: `gyr_cov=0.5`면 자이로를 덜 신뢰해 회전 추정이 라이다 매칭에만 의존 → 회전 시 드리프트. → **0.1로 되돌려 회전 드리프트 22m→1.3m.**
- **남은 문제 — 빠른 회전**: 위 3개 적용 후 직진/단순회전은 OK였으나, **복합 주행에서 여전히 발산.** 발산 시점이 IMU 자이로 최대값(1.685 rad/s ≈ 97°/s) 구간과 정확히 일치. 즉 **가장 빠르게 회전한 순간 라이다 매칭 실패 → 보행 가속도(최대 27.9 m/s², 중력의 3배)가 IMU 단독 적분되어 폭주.** 이는 4족로봇+10Hz 라이다 LIO의 구조적 약점.
  - `point_filter_num=2`,`max_iteration=4`로 매칭 강화 시도 → **실패(여전히 발산).**
  - 오프라인 bag 재생이 CPU 부하로 일관성 부족(같은 데이터인데 발산 시점 22s/15s 변동) → 오프라인 튜닝 신뢰도 낮음. **CPU 부하부터 줄여야 함.**

---

## 7. 지금 막힌 지점 (BLOCKER)
빠른-회전 발산 대책으로 **라이다를 20Hz(`1024x20`)로 바꾸려고 `lidar_mode` 변경 → 라이다가 응답 불능**.
- 증상: `ping` 실패, HTTP API(`169.254.6.117/api/v1/...`) timeout, ARP는 한때 REACHABLE이나 ICMP/HTTP 60초+ 무응답.
- 2026-06-16 재확인: `enx00e099010d5f`는 `UP, LOWER_UP`, 호스트 IP `169.254.0.2/16` 정상. UDP 버퍼 `8388608` 정상. 설정 파일도 `src`/`install` 동기화됨. 하지만 `ping`/HTTP 실패, ARP는 `INCOMPLETE` 또는 MAC 표시 후 지연 상태라 매핑 런치 불가.
- 해석: 이더넷 칩엔 전원 있으나 센서 본체가 hang/부팅실패. **물리적 파워 사이클 필요(소프트웨어로 복구 불가).**
- 의심: 라이다 전원 공급 불안정 — 작업 내내 `poll_client() timed out`이 간헐적으로 떴고 결국 완전 정지. Go2 배터리 잔량/전원 커넥터 접촉/과열 의심.
- **사용자 조치 대기 중**: OS1 전원 차단 5~10초 후 재연결 → ~1분 부팅.

### 라이다 복구 확인 명령
```bash
ping -c3 169.254.6.117
curl -s http://169.254.6.117/api/v1/sensor/metadata/sensor_info | head -c 100   # JSON 나오면 정상
```

---

## 8. 다음 단계 (우선순위 순)
1. **라이다 복구 확인** (7장 명령). 안 되면 사용자에게 전원/케이블/과열 점검 요청.
2. **20Hz 발산 테스트**: 현재 `lidar_mode='1024x20'`, `scan_rate=20` 설정됨. 드라이버 띄워 데이터레이트 20Hz 확인 → 복합주행(빠른 회전 포함) 재테스트. 프레임간 회전각이 절반이 되어 빠른 회전에 강건해질 것으로 기대.
   - **테스트 전 사용자에게 원격 스트리밍/VSCode 등 CPU 부하 줄이도록 요청** (CPU 경쟁이 발산·재생 일관성에 영향).
3. 20Hz로도 발산하면 → **Go2 leg odometry EKF 융합** (9장). 다리로봇 LIO의 근본 해법.
4. 발산 안정화되면 → **PGO 루프클로저 검증**: 출발점 1m 이내 복귀하는 루프 주행 → `/pgo/loop_markers`에 엣지 생성 + `map→body` tf offset이 0이 아니게 변하는지 확인. (주의: `loop_search_radius=1.0m`라 드리프트가 1m 넘으면 못 잡음 → 필요시 키울 것.)
5. PGO 보정맵 저장 → **Nav2 연계**: 3D→2D occupancy grid 변환, `map_server`+AMCL, Go2 SportClient↔`cmd_vel` 브릿지.

---

## 9. 미착수 — Go2 leg odometry EKF 융합 (사용자 원래 제안 아키텍처)
빠른 회전 발산의 근본 해법 후보. LIO가 순간 발산해도 leg odom이 잡아줌.
```
Ouster LiDAR+IMU → FAST-LIO2 odometry ─┐
Go2 IMU / leg odometry ────────────────┤→ robot_localization EKF → 융합 pose
```
- Go2 데이터 소스: `/lowstate`(`unitree_go/msg/LowState`)의 `imu_state`, `/sportmodestate`(`unitree_go/msg/SportModeState`)의 `position`/`velocity`/`yaw_speed`/`foot_force` 등. **표준 `sensor_msgs/Imu`,`nav_msgs/Odometry`가 아니므로 변환 브릿지 노드 필요.**
- `robot_localization` 패키지로 EKF 구성.

---

## 10. 실행 방법
`.bashrc`에 `source /opt/ros/humble/setup.bash`,`source ~/go2_ws/install/setup.bash` 이미 포함 → 새 터미널은 바로 `ros2` 사용 가능.

**매 세션 1회 (재부팅 시 필수):**
```bash
sudo sysctl -w net.core.rmem_max=8388608
sudo sysctl -w net.core.rmem_default=8388608
```

**통합 실행 (권장):**
```bash
ros2 launch ~/go2_ws/go2_mapping.launch.py            # RViz 포함
ros2 launch ~/go2_ws/go2_mapping.launch.py rviz:=false # CPU 절약
```

**복구 확인 후 자동 실행 (권장, 2026-06-16 추가):**
```bash
~/go2_ws/scripts/go2_mapping_ready.sh
RVIZ=true ~/go2_ws/scripts/go2_mapping_ready.sh   # 필요할 때만 RViz 포함
```
- 이 스크립트는 인터페이스/IP, UDP 버퍼, `src`↔`install` 설정 동기화, 20Hz 핵심 설정, 라이다 ping+HTTP metadata 응답을 확인한 뒤에만 통합 launch를 실행한다.
- 라이다가 응답하지 않으면 launch를 시작하지 않고 전원 재인가가 필요하다는 에러로 종료한다.

**개별 실행 (디버깅용, 터미널 3개):**
```bash
ros2 launch ouster_ros driver.launch.py viz:=false
ros2 launch fast_lio mapping_ouster64.launch.py rviz:=false   # +point_filter_num:=N max_iteration:=N 등 인자 가능
ros2 run pgo pgo_node --ros-args -p config_path:=$HOME/go2_ws/install/pgo/share/pgo/config/pgo.yaml
```

**맵 저장:**
- FAST-LIO 단독 맵: FAST_LIO 노드 Ctrl+C 시 자동 저장 → `~/go2_ws/src/FAST_LIO/PCD/result.pcd`, `traj/trajectory.txt`. (단, **발산 상태로 종료하면 저장 안 됨**.)
- PGO 보정 맵 (서비스 호출):
```bash
ros2 service call /pgo/save_maps interface/srv/SaveMaps "{file_path: '/home/ria4065/go2_ws/src/FAST_LIO/PCD', save_patches: false}"
# → PCD/map.pcd (보정맵) + poses.txt
```

**저장된 PCD 보기:**
```bash
ros2 run pcl_ros pcd_to_pointcloud --ros-args -p file_name:=$HOME/go2_ws/src/FAST_LIO/PCD/result.pcd
ros2 run rviz2 rviz2   # PointCloud2 추가, topic=/cloud_pcd, Fixed Frame=base_link
```

---

## 11. 주요 토픽 / 프레임
- 드라이버: `/ouster/points`(PointCloud2, ~10Hz→20Hz), `/ouster/imu`(100Hz)
- FAST-LIO: `/Odometry`(nav_msgs/Odometry, frame `camera_init`→`body`), `/cloud_registered`(등록 스캔), `/cloud_registered_body`(body frame, **PGO 입력**), `/Laser_map`(누적맵, 시각화용), `/path`
- PGO 입력 리매핑: `pgo.yaml`의 `cloud_topic=/cloud_registered_body`, `odom_topic=/Odometry`, `local_frame=body`
- PGO 출력: `/pgo/loop_markers`(MarkerArray), `map→body` tf, 서비스 `/pgo/save_maps`

---

## 12. 현재 설정값 (확인됨, 2026-06-16)
**`src/ouster-ros/ouster-ros/config/driver_params.yaml`**
```
sensor_hostname: '169.254.6.117'
udp_dest: '169.254.0.2'
lidar_mode: '1024x20'              # 20Hz 테스트용 (직전 변경, 라이다 응답불능 트리거)
timestamp_mode: 'TIME_FROM_INTERNAL_OSC'   # ★ 발산해결 핵심, 되돌리지 말 것
point_cloud_frame: os_sensor      # ★ 발산해결 핵심(180° 버그), 되돌리지 말 것
use_system_default_qos: true      # ★ QoS 매칭, 되돌리지 말 것
point_type: original
```
**`src/FAST_LIO/config/ouster64.yaml`**
```
lid_topic: /ouster/points,  imu_topic: /ouster/imu
blind: 0.7,  scan_rate: 20      # scan_rate는 lidar_mode와 일치시킬 것 (20Hz면 20)
acc_cov: 0.1, gyr_cov: 0.1, b_acc_cov: 0.0001, b_gyr_cov: 0.0001   # ★ 회전 안정화, 되돌리지 말 것
extrinsic_T: [0.002441, 0.009725, -0.007533]   # Ouster IMU lever-arm
extrinsic_R: identity
pcd_save_en: true, traj_save_en: true
```
**`src/pgo/config/pgo.yaml`**: `cloud_topic=/cloud_registered_body`, `odom_topic=/Odometry`, `local_frame=body`, `loop_search_radius=1.0`.

---

## 13. 알려진 함정 (반드시 숙지)
1. **symlink-install 깨짐**: `livox_ros_driver2/build.sh`가 전체 워크스페이스를 symlink 없이 colcon build → `install/*/share/*/config/*.yaml`이 symlink에서 일반 복사본으로 바뀜. **그 이후로 `src`에서 yaml을 고쳐도 install에 반영 안 됨.** → config 수정 후 반드시 `cp src경로 install경로`로 복사하거나 `ls -la`로 symlink 여부 확인. (이 문서의 모든 config 변경은 이 방식으로 install에 반영해 왔음.)
2. **터미널 닫으면 노드 죽음**: 드라이버/노드를 띄운 터미널 창을 닫으면 SIGHUP으로 프로세스 종료 → "데이터 없는데 토픽은 잔상으로 남아" 가짜 디버깅 유발. 매핑 끝까지 창 유지하거나 `nohup`/별도 탭 사용.
3. **`ros2 topic hz`가 이 환경에서 출력 없이 죽는 경우 많음** → `ros2 topic echo <topic> --field <f> --once`로 확인.
4. **발산하면 그 세션 복구 불가** → 노드 재시작 필요. 발산 판정: `ros2 topic echo /Odometry --field pose.pose.position --once`가 수백~수천 m이면 발산. (정상은 한 자리~십 m.) FAST_LIO 로그의 `No Effective Points!` 반복도 발산 신호.
5. **CPU 경쟁**: 원격 데스크톱 스트리밍(`nxcodec.bin`/`nxnode.bin`)이 CPU 70%+ 점유 → 시간정렬·재생 일관성 악화. 테스트 전 줄이도록 사용자에게 요청.
6. **라이다 전원 불안정 의심** (7장). `poll_client timed out`이 반복되면 하드웨어 점검 필요.

---

## 14. 진단 도구
- 발산 실시간 감시: `for i in $(seq 1 12); do ros2 topic echo /Odometry --field pose.pose.position --once; sleep 2; done`
- IMU 스파이크 분석(녹화 bag): `python3 /home/ria4065/go2_ws/bags/analyze_imu.py` (가속도/자이로 norm 구간별 최대값 출력)
- bag 정보: `ros2 bag info /home/ria4065/go2_ws/bags/diverge_test`
- 발산 데이터 오프라인 재현: FAST_LIO 띄운 뒤 `ros2 bag play /home/ria4065/go2_ws/bags/diverge_test` (단, CPU 부하 시 비일관 — 13.5 참고)

---

## 15. 관련 문서
- `MAPPING_PLAN.md` — 더 이른 시점의 한국어 계획서(일부 내용은 이 문서가 최신). 겹치면 **이 `agent_plan.md`가 우선.**

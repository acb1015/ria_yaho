# Go2 + Orin NX + Ouster OS1 매핑 계획

작성일: 2026-06-16 (최종 수정: 2026-06-16)

## 0. 목표 및 현재까지의 범위

**오늘 목표**: 사람이 Go2를 원격조종(리모컨/앱)으로 직접 몰면서, OS1 라이다 기반 실시간 LIO로 지도를 만든다.

- ✅ 달성: 실시간 LIO가 발산 없이 정상 동작 확인, 맵 저장/시각화까지 성공
- ⚠️ **아직 아님**: 지금 만든 맵은 "raw 3D 포인트클라우드" 단계이며 **그대로 Nav2 자율주행에 못 씀**. 네비게이션까지 가려면 루프클로저(PGO), 2D 점유격자 변환, map_server+AMCL, Go2 cmd_vel 브릿지가 추가로 필요 (7장 참고)
- 로봇 이동 자체는 Go2 리모컨/공식 앱으로 수행, Orin NX의 ROS2 스택은 "센서 구동 + LIO 매핑(+추후 PGO)"만 담당

---

## 1. 현재 환경 상태

| 항목 | 상태 | 비고 |
|---|---|---|
| Go2 DDS 연결 (`unitree_ros2`, `unitree_sdk2`) | ✅ 완료 | `eno1` (192.168.123.1/24) |
| OS1-64 라이다 (`ouster_ros`) | ✅ 완료 | 전용 USB-Ethernet `enx00e099010d5f` (169.254.0.2) |
| ROS2 배포판 | Humble | |
| LIO (`fast_lio`, `livox_ros_driver2`) | ✅ 완료, **실제 주행 검증 성공** | Taeyoung96/FAST_LIO_ROS2 기반, `config/ouster64.yaml` |
| 루프클로저(PGO) | 🔵 진행 중 (다음 단계) | liangheming/FASTLIO2_ROS2의 `pgo`+`interface` 패키지 재사용 예정 |
| Nav2 연계 | ⬜ 미착수 | 7장 "추후 단계" |

### OS1 센서 정보
모델: OS1-64-U13-SR (S/N 122619005017), 펌웨어 v3.1.0, lidar_mode `1024x10`

---

## 2. 사용 중인 패키지

| 구성 요소 | 패키지 | 역할 |
|---|---|---|
| 로봇 통신 | `unitree_ros2`, `unitree_sdk2` 등 | DDS 통신 (모니터링용, 주행 명령엔 안 씀) |
| 라이다 드라이버 | `ouster_ros`, `ouster_sensor_msgs` | OS1 포인트클라우드/IMU 퍼블리시 |
| **LIO** | **[Taeyoung96/FAST_LIO_ROS2](https://github.com/Taeyoung96/FAST_LIO_ROS2)** (`fast_lio`, `livox_ros_driver2`) | 실시간 오도메트리 + 정합 맵, `config/ouster64.yaml`로 OS1-64 네이티브 지원 |
| 맵 저장 | FAST_LIO 자체 PCD/궤적 export (`pcd_save_en`/`traj_save_en`) | `Ctrl+C`(SIGINT) 시 자동 저장 |
| **루프클로저(예정)** | `liangheming/FASTLIO2_ROS2`의 `pgo` + `interface` 패키지 | GTSAM 기반 pose graph 최적화. **Livox 프론트엔드 없이도** `/lio/odom`(nav_msgs/Odometry), `/lio/body_cloud`(sensor_msgs/PointCloud2) 일반 토픽만 구독해서 동작 → 우리 FAST_LIO 출력을 리매핑해서 바로 연결 가능 |

### 검토했지만 보류/탈락한 것
- **liangheming/FASTLIO2_ROS2의 `fastlio2`(프론트엔드)**: `livox_ros_driver2::msg::CustomMsg` 전용이라 Ouster와 호환 안 됨 → 프론트엔드는 안 쓰고 **`pgo` 모듈만 재사용**하는 쪽으로 결정
- **rohrschacht/FAST_LIO_SLAM_ros2**: 이름은 "FAST-LIO+SC-PGO"지만 실제 내용 확인 결과 SC-PGO 없이 **FAST-LIO 단독 포팅본**이었음 (서브모듈에 ikd-Tree만 있고 SC-PGO 없음) → 탈락
- DLIO, KISS-ICP: Ouster 네이티브 지원이 확실한 FAST_LIO_ROS2로 먼저 검증 완료, 추가 비교는 보류

---

## 3. 단계별 실행 계획

### Phase 0 — 환경 정정 ✅ 완료
- [x] [setup.sh](src/unitree_ros2/setup.sh) / [setup_default.sh](src/unitree_ros2/setup_default.sh) 를 Humble + `eno1` 기준으로 수정
- [x] DDS 연결 검증 (`ros2 daemon stop` 후 `ros2 topic list`)
- [x] Jetson 성능모드 고정 (`nvpmodel -m 0` → MAXN)
- [x] OS1 시간 동기화: `timestamp_mode: 'TIME_FROM_ROS_TIME'`

### Phase 1 — 센서 단독 구동 검증 ✅ 완료
- [x] OS1 단독 구동, `/ouster/points`(10Hz), `/ouster/imu`(100Hz) 확인
- [x] UDP 수신버퍼 부족으로 포인트레이트 저하 → `net.core.rmem_max=8388608` 적용

### Phase 2 — LIO 패키지 설치 ✅ 완료
- [x] `Taeyoung96/FAST_LIO_ROS2` 설치, `src/` 바로 아래 구조로 재배치, Livox-SDK2 시스템 설치, `ouster64.yaml` 토픽/저장경로 수정
- (버그 상세는 6장 참고)

### Phase 3 — 최소 TF 설정 ⬜ 보류
- [ ] `base_link → os_sensor` 정적 TF 작성 — 오늘은 매핑 자체 검증에 집중, TF는 Nav2 연계 단계에서 다시 다룸

### Phase 4 — 통합 Launch 구성 ⬜ 보류
- [ ] 지금은 터미널 2개로 따로 실행 중 (5장 참고). 안정화되면 launch 파일로 통합

### Phase 5 — 현장 테스트 ✅ 완료 (성공)
- [x] 좌표계 버그 수정 후 실제 주행 테스트 성공 (약 14m 이동, 발산 없음)
- [x] RViz/PCL 시각화로 맵 형태 확인 (벽/바닥 구조 인식 가능한 수준)
- [x] PCD(307MB, 962만 포인트)/궤적(65 포즈) 저장 성공

### Phase 6 — 루프클로저(PGO) 추가 🔵 다음 단계
- [ ] `sudo apt install ros-humble-gtsam`
- [ ] `liangheming/FASTLIO2_ROS2`에서 `pgo`, `interface` 패키지만 `src/`에 추가
- [ ] PGO 설정의 구독 토픽을 우리 FAST_LIO 출력으로 리매핑: `/lio/odom` ← `/Odometry`, `/lio/body_cloud` ← `/cloud_registered_body`
- [ ] 빌드, 기존 파이프라인과 같이 구동
- [ ] 같은 장소를 재방문하는 주행으로 루프클로저 동작(맵 보정) 확인

---

## 4. 실행 방법

`.bashrc`에 `source /opt/ros/humble/setup.bash`, `source ~/go2_ws/install/setup.bash`가 이미 들어있어 새 터미널에서 별도 source 불필요.

### 매핑 세션 전 한 번 확인 (재부팅했다면 필수)
```bash
sudo sysctl -w net.core.rmem_max=8388608
sudo sysctl -w net.core.rmem_default=8388608
```

### 터미널 1 — OS1 라이다 드라이버 (창 닫지 말 것)
```bash
ros2 launch ouster_ros driver.launch.py viz:=false
```

### 터미널 2 — FAST_LIO 매핑 (창 닫지 말 것)
```bash
ros2 launch fast_lio mapping_ouster64.launch.py        # RViz 포함
ros2 launch fast_lio mapping_ouster64.launch.py rviz:=false   # CPU 절약, RViz 없이
```
처음 몇 초는 로봇을 가만히 두고 `IMU Initial Done`, `Initialize the map kdtree` 확인 후 움직이기 시작.

### 정상 동작 확인용 명령
```bash
ros2 topic hz /ouster/points     # ~10Hz
ros2 topic hz /Odometry          # ~10Hz
ros2 topic echo /Odometry --field pose.pose.position --once   # 발산 여부 체크(수십~수백m 이상이면 발산)
ros2 topic echo /Laser_map --field width --once               # 누적 포인트 수 증가 확인
```

### 종료 (저장)
터미널 2에서 `Ctrl+C` → 자동 저장:
- 지도: `~/go2_ws/src/FAST_LIO/PCD/result.pcd`
- 궤적: `~/go2_ws/src/FAST_LIO/traj/trajectory.txt`

⚠️ 발산된 상태로 끝내면 저장이 씹히는 경우가 있었음 (6장 참고) — 발산 징후 있으면 저장하지 말고 재시작.

### 저장된 맵 다시 보기
```bash
ros2 run pcl_ros pcd_to_pointcloud --ros-args -p file_name:=$HOME/go2_ws/src/FAST_LIO/PCD/result.pcd
ros2 run rviz2 rviz2   # PointCloud2 디스플레이 추가, Topic=/cloud_pcd, Fixed Frame=base_link
```

---

## 5. 오늘 발견한 버그/이슈 전체 정리

1. **`unitree_ros2` setup 스크립트**: foxy/`enp3s0` 하드코딩 → humble/`eno1`로 수정
2. **UDP 수신버퍼 부족**: `net.core.rmem_max` 212992B → 8388608B로 증설 (포인트레이트 6.7Hz→10Hz)
3. **FAST_LIO_ROS2 빌드 위치**: `src/` 바로 아래로 재배치 필요
4. **Livox-SDK2 미설치**: 소스 빌드 후 `sudo make install`
5. **`ouster64.yaml` 토픽명**: ROS1 시절 이름 → `/ouster/points`, `/ouster/imu`로 수정
6. **파라미터 타입 에러**: `extrinsic_R`이 정수 표기라 `double_array`와 충돌 → 소수점 추가
7. **QoS 불일치**: ouster_ros BEST_EFFORT vs FAST_LIO RELIABLE → `use_system_default_qos: true`
8. **`ring` 필드 타입 불일치**: FAST_LIO 내장 구조체 `uint8_t` vs 실제 드라이버 `uint16_t` → 소스 수정 후 재빌드
9. **symlink-install 깨짐**: `livox_ros_driver2/build.sh`가 전체를 symlink 없이 재빌드하면서 기존 symlink 설정 파일들이 일반 복사본으로 바뀜 → 설정 변경이 반영 안 되는 일이 반복 발생. 적용 안 되면 `ls -la install/<pkg>/share/<pkg>/config/*.yaml`로 symlink 여부 먼저 확인
10. **"가짜 매핑 실패" (버그 아님)**: 드라이버를 띄운 터미널을 닫아서 `os_driver` 프로세스가 같이 죽었는데, `ros2 topic list`엔 잔상이 남아 헷갈림 → `ros2 topic hz`로 실제 데이터 흐름 확인 필요. **드라이버/FAST_LIO 실행 터미널은 매핑 끝날 때까지 닫지 말 것**
11. **CPU 과부하**: 원격화면 스트리밍(`nxcodec.bin`/`nxnode.bin`) + VSCode `cpptools` 인덱싱이 CPU를 많이 먹어서 라이다 패킷 처리가 밀리는 현상 → 매핑 중엔 무거운 백그라운드 작업 자제, RViz도 끄면 도움
12. **★ 좌표계 180도 회전 버그 (가장 중요)**: `driver_params.yaml`의 `point_cloud_frame: os_lidar`로 포인트클라우드를 발행하고 있었는데, `os_lidar`는 `os_sensor` 기준 **Z축 180도 회전**된 프레임이고 `os_imu`는 회전 없음(identity). FAST_LIO의 `extrinsic_R`은 라이다-IMU 간 회전차가 없다고 가정(identity)하므로 실제로는 180도 차이가 나는 걸 무시하게 됨. 정지 시엔 안 드러나지만 회전 움직임이 생기면 즉시 오도메트리가 발산(좌표값이 수천 단위로 폭주). **`point_cloud_frame: os_sensor`로 변경**해서 IMU와 같은 회전 기준으로 맞춰서 해결
13. **IMU 공분산/blind 튜닝**: 4족 보행 진동 대응 위해 `acc_cov`/`gyr_cov` 0.1→0.5, `b_acc_cov`/`b_gyr_cov` 0.0001→0.001, `blind` 2.0→0.7m로 조정 (12번 버그 고치기 전에 적용했던 거라 단독 효과는 불확실하지만 유지 중)
14. **저장 실패 패턴**: 발산한 상태에서 Ctrl+C(또는 강제종료)하면 `pcd_save`/`traj_save` 코드까지 못 가고 파일이 갱신 안 되는 경우 있었음 → 발산 확인되면 저장 기대하지 말고 재시작

---

## 6. 다음 단계: 루프클로저(PGO) 통합 상세 계획

목표: 같은 공간을 여러 번 지나가도 맵이 어긋나지 않고 정합되도록(드리프트 보정) `pgo` 백엔드 추가

1. `sudo apt install ros-humble-gtsam`
2. `liangheming/FASTLIO2_ROS2` 클론 → `pgo/`, `interface/` 디렉토리만 추출해서 `go2_ws/src/`에 배치
3. `interface` 패키지가 Livox 의존성 없는지 확인 (메시지/서비스 정의만 있을 가능성 높음)
4. PGO 설정 yaml에서 토픽 리매핑:
   - `/lio/odom` ← 우리 `/Odometry`
   - `/lio/body_cloud` ← 우리 `/cloud_registered_body`
5. `colcon build --packages-select interface pgo`
6. 기존 ouster_ros + fast_lio 파이프라인 위에 pgo 노드 추가 실행
7. 같은 구간을 다시 지나가는 주행으로 `/pgo/loop_markers` 발생 및 맵 보정 확인
8. 보정된 맵 저장 기능(서비스) 확인

---

## 7. 추후 단계 (Nav2 자율주행 연계, 오늘/PGO 이후 범위)
- 3D 맵 → 2D 점유격자(occupancy grid)/costmap 변환
- `map_server` + AMCL(또는 동급) 위치추정 구성
- `base_link → os_sensor` 정밀 정적 TF (Phase 3에서 보류한 것)
- Go2 SportClient ↔ Nav2 `cmd_vel` 브릿지 노드 작성

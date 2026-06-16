# Go2 + Orin NX + Ouster OS1 실시간 SLAM 매핑 계획

작성일: 2026-06-16
목적: Unitree Go2(Orin NX 탑재) + Ouster OS1-64 라이다를 이용한 **실시간 LiDAR-Inertial SLAM** 구축, 추후 Nav2 기반 자율주행 연계

---

## 1. 현재 환경 상태

| 항목 | 상태 | 비고 |
|---|---|---|
| Go2 DDS 연결 (`unitree_ros2`, `unitree_sdk2`) | ✅ 빌드 완료 | `eno1` (192.168.123.1/24) 로 로봇 내부망 연결 |
| OS1-64 라이다 (`ouster-ros`) | ✅ 빌드 완료 | 전용 USB-Ethernet `enx00e099010d5f` (169.254.0.2) 로 연결, 메타데이터(`169.254.6-metadata.json`) 수집 완료 |
| ROS2 배포판 | Humble | 시스템에 설치되어 사용 중 |
| 실시간 SLAM/오도메트리 패키지 | ❌ 없음 | `ouster-sdk` 내 `ouster_mapping`(kiss-icp 기반)은 ROS 노드로 미연결, 오프라인 CLI용이라 그대로 쓰기 어려움 |

### ⚠️ 발견된 버그 (Phase 0에서 즉시 수정 필요)
- [src/unitree_ros2/setup.sh](src/unitree_ros2/setup.sh), [src/unitree_ros2/setup_default.sh](src/unitree_ros2/setup_default.sh) 가
  - `/opt/ros/foxy/setup.bash` 를 source (실제는 **Humble**)
  - CycloneDDS 네트워크 인터페이스가 `enp3s0` 로 하드코딩 (실제는 **eno1**)
- → 수정 전엔 로봇과 DDS 통신이 되지 않음.

### OS1 센서 주요 설정값 (메타데이터 기준)
- 모델: OS1-64-U13-SR (S/N 122619005017), 펌웨어 v3.1.0
- lidar_mode: `1024x10` (1024 columns x 10Hz)
- timestamp_mode: `TIME_FROM_INTERNAL_OSC` (호스트와 시간 미동기화 상태 — 정밀 융합 시 보정 필요)
- udp_dest: `169.254.0.2` (Orin NX의 전용 인터페이스, 일치 확인됨)

---

## 2. 사용할 패키지 / 알고리즘 정리

| 구성 요소 | 패키지 | 역할 | 상태 |
|---|---|---|---|
| 로봇 통신 | `unitree_ros2`, `unitree_sdk2`, `unitree_api`, `unitree_go`, `unitree_hg` | Go2 상태/제어 DDS 통신 | 이미 워크스페이스에 있음 |
| 라이다 드라이버 | `ouster_ros`, `ouster_sensor_msgs` | OS1 포인트클라우드/IMU 퍼블리시 | 이미 워크스페이스에 있음 |
| **LiDAR-Inertial Odometry/SLAM** | **FAST-LIO2 (ROS2 포트)** ← 1순위 추천 | 실시간 오도메트리 + 정합 맵 생성 | **신규 추가 필요** |
| (대안 1) | DLIO (Direct LiDAR-Inertial Odometry, ROS2 브랜치) | 정확도는 더 좋으나 연산량↑, Orin NX엔 부담 가능 | 미사용(대안) |
| (대안 2) | KISS-ICP (ROS2 wrapper) | 라이다 단독, IMU 미사용 → 가장 가볍지만 드리프트에 불리 | 미사용(대안) |
| TF/캘리브레이션 | `static_transform_publisher` (또는 robot URDF) | `base_link → os_sensor` 외부 캘리브레이션 | 신규 작성 필요 |
| 2D 맵 변환 (Nav2용) | `pointcloud_to_laserscan` 또는 `nav2_costmap_2d` voxel layer | 3D 포인트클라우드 → 2D occupancy grid / costmap | 추후 단계에서 추가 |
| 자율주행 | `nav2_*` (map_server, AMCL/localization, planner, controller) | 저장된 맵 기반 자율주행 | 추후 단계 |
| 로봇-Nav2 브릿지 | 신규 작성 (Go2 SportClient ↔ `cmd_vel`) | Nav2 명령을 Go2 보행 명령으로 변환 | 추후 단계 |

**LIO 알고리즘 선정 이유 (FAST-LIO2):**
- Jetson류 임베디드 보드에서 실전 검증된 사례가 많고 연산량이 가벼움
- OS1 IMU와 타이트 커플링(tightly-coupled) 가능 → 4족 보행 진동 환경에서도 비교적 안정적
- 추후 Nav2 연계를 염두에 둔 실시간 처리 요구사항에 적합

---

## 3. 단계별 실행 계획

### Phase 0 — 환경 정정 (선결 작업)
- [ ] `setup.sh` / `setup_default.sh` 를 Humble + `eno1` 기준으로 수정
- [ ] Jetson 성능모드 고정: `sudo nvpmodel -m 0 && sudo jetson_clocks`
- [ ] OS1 시간 동기화 점검 (`TIME_FROM_PTP_1588` 전환 검토, 또는 드라이버 수신시각 기반 보정)

### Phase 1 — 센서 단독 구동 검증
- [ ] `ros2 launch ouster_ros sensor.launch.xml` 로 OS1 단독 구동
- [ ] `/ouster/points`, `/ouster/imu` 토픽 발행 확인, RViz로 포인트클라우드 시각 확인
- [ ] IMU 데이터 레이트/노이즈 확인

### Phase 2 — 로봇 연결 검증
- [ ] `unitree_ros2/example` 의 `read_low_state` / `read_motion_state` 노드로 Go2 IMU·관절·바디 오도메트리 토픽 수신 확인
- [ ] 추후 LIO 결과와 로봇 자체 foot odometry 비교용 베이스라인 확보

### Phase 3 — 외부 캘리브레이션 (TF)
- [ ] OS1 장착 위치/각도 실측 → `base_link → os_sensor` 정적 TF 작성
- [ ] Go2 공식 URDF가 있으면 라이다 마운트 추가, 없으면 간단 xacro 신규 작성

### Phase 4 — LIO/SLAM 패키지 도입
- [ ] FAST-LIO2 ROS2 포트 워크스페이스에 추가
- [ ] OS1 포인트 포맷(필드명, ring/timestamp)에 맞게 컨피그 수정
- [ ] 빌드 및 단독 구동 확인

### Phase 5 — 통합 Launch 구성
- [ ] OS1 드라이버 → static TF → LIO 노드 → RViz 순으로 한 번에 기동하는 launch 파일 작성
- [ ] `/Odometry`(또는 동급), 정합된 `/cloud_registered`(map frame) 토픽 확인

### Phase 6 — 현장 테스트
- [ ] 로봇 정지 상태에서 IMU 바이어스/정렬 안정화 확인
- [ ] 저속 보행으로 단순 루프(직사각형 경로) 매핑 테스트
- [ ] 드리프트, 루프 닫힘, 보행 진동에 의한 포인트클라우드 흔들림 점검 → 디스큐/IMU 프리인테그레이션 파라미터 튜닝

### Phase 7 — 자율주행 연계 준비 (Nav2)
- [ ] 3D 포인트클라우드 맵 → 2D occupancy grid / costmap 변환
- [ ] 저장된 LIO 맵으로 Nav2 `map_server` + AMCL/localization 구성
- [ ] Go2 SportClient ↔ Nav2 `cmd_vel` 브릿지 노드 작성

---

## 4. 참고
- 본 계획은 실시간 SLAM 구축 후 추후 Nav2 자율주행 연계를 목표로 함 (오프라인 정밀 3D 맵 생성이 목표라면 Phase 4~7 접근 방식이 달라짐)
- Phase 0, 1은 현재 워크스페이스에서 즉시 실행 가능

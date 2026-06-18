# Go2 Local Traversability 파이프라인 작업 로그 (chomo.md)

> 이 문서는 진행한 작업을 **순서대로** 기록한다. 새 작업을 할 때마다 해당 단계 섹션을 추가/갱신한다.

## 전체 목표 파이프라인
```
Ouster (/ouster/points)
  → elevation_mapping_cupy            ← 현재 집중 대상 (2.5D 맵 결과까지가 1차 목표)
  → traversability (내장 NN 필터)
  → GridMap → OccupancyGrid 변환 노드
  → Nav2 local costmap
  → Nav2 controller
```

## 현재 1차 목표
**elevation_mapping_cupy로 2.5D elevation map 결과를 RViz/토픽으로 확인하는 것까지.**
이게 잘 되면 그 다음(traversability → occupancy → Nav2)으로 진행한다.

## 환경 요약
- HW: Jetson (JetPack 6 / L4T R36.5, CUDA 12.6, aarch64)
- ROS2 Humble / Ubuntu 22.04, workspace: `~/go2_ws`
- LiDAR: Ouster OS-1-64 (`169.254.6.117`, USB-eth `enx00e099010d5f` = 169.254.0.2)
- Odometry: FAST_LIO (ROS2, `fast_lio` 패키지), config `ouster64.yaml`

---

## 1단계 — Ouster 드라이버 검증 ✅
- `ros2 launch ouster_ros driver.launch.py viz:=false` 로 기동.
- 센서: OS-1-64-U13-SR, firmware 3.1.0, lidar_mode 1024x10.
- 확인된 토픽: `/ouster/points`(frame `os_sensor`, width 1024, **best-effort QoS**), `/ouster/imu`(frame `os_imu`).
- 주의: `timestamp_mode: TIME_FROM_INTERNAL_OSC` → 스탬프가 센서 내부 클럭(부팅 후 경과초). 나중에 Nav2/TF 시간정합 단계에서 `TIME_FROM_ROS_TIME` 등으로 조정 검토.

## 2단계 — FAST_LIO odometry + TF 브리지 ✅
- `ros2 launch fast_lio mapping_ouster64.launch.py rviz:=false` 기동.
- 발행: `/Odometry`(frame `camera_init` → child `body`), `/path`, TF `camera_init→body`.
- **문제 발견**: Ouster TF 트리(`os_sensor→{os_imu,os_lidar}`)와 FAST_LIO 트리(`camera_init→body`)가 **단절** → elevation mapping이 `os_sensor` 포인트를 맵 프레임으로 변환 불가.
- **해결**: `body→os_sensor` static TF 추가 (FAST_LIO `body` ≡ Ouster `os_imu`이므로 `os_sensor→os_imu`의 역변환 사용).
  - 값: `x=0.002441 y=0.009725 z=-0.007533`, 회전 identity.
- 결과: `camera_init → body → os_sensor → {os_imu, os_lidar}` 전체 체인 연결 확인.

## 3단계 — bringup 패키지로 영구화 ✅
- 새 패키지 `src/go2_traversability` 생성 (ament_cmake).
- `launch/sensor_odom_bringup.launch.py`: Ouster 드라이버 + FAST_LIO + `body→os_sensor` static TF를 한 번에 기동.
- 실행: `ros2 launch go2_traversability sensor_odom_bringup.launch.py` (옵션 `viz:=true`).

## 4단계 — GPU(python) 의존성 정렬 ✅
- cupy/numpy 충돌 정리. ROS2 Humble은 numpy 1.x ABI 기준이라 numpy 2.x는 위험.
- 최종: `numpy==1.24.4`, `cupy-cuda12x==13.6.0`, `fastrlock`, `scipy 1.8`(system) 모두 호환.
  - numpy 1.24.4 선택 이유: cupy(>=1.22)·scipy(<1.25)·ROS(1.21 빌드 ABI) 셋 다 만족.
- 검증: cupy GPU 연산 OK, rclpy/point_cloud2 OK.
- 설치 위치: `~/.local`(--user) — 시스템 비침투, 제거 가능.

## 5단계 — elevation_mapping_cupy 준비 ✅
- 저장소 clone: `src/elevation_mapping_cupy` → **`ros2` 정식 브랜치**(ament_cmake) 사용. (main은 ROS1/catkin.)
- 추가 clone: `src/ros2_numpy`(Box-Robotics) — apt에 없어 소스 빌드.
- python 의존성(--user): `simple-parsing`, `shapely<2`(1.8.5), `scikit-learn`.
- **apt(사용자 실행 완료)**: `ros-humble-grid-map`, `ros-humble-tf-transformations`.
- Go2용 config 작성: `elevation_mapping_cupy/.../config/setups/go2/base.yaml`
  - `/ouster/points` 구독, `map_frame: camera_init`, `base_frame: body`, publishers에 `elevation`/`traversability` 레이어.
- 확인: EMC 포인트클라우드 구독 QoS = `sensor_data`(best-effort) → Ouster와 매칭 OK (QoS 문제 없음).

## 6단계 — torch 우회 + 빌드 + 라이브 실행 (2.5D 달성) ✅
**목표를 "2.5D elevation 먼저"로 한정. traversability(torch)는 다음 단계로 연기.**

1. **torch 우회 (스텁)**: JetPack6 CUDA torch 휠 인덱스(jetson-ai-lab)가 이 Jetson에서 접근 불가(HTTP 000). 내장 traversability는 torch 필수이므로, 코드에 **cupy 패스스루 스텁**을 추가해 torch 없이 노드 기동.
   - `traversability_filter.py`: `PassthroughTraversabilityFilter`(+`get_filter_passthrough`) 추가 — traversability=1.0 반환, NN 필터와 동일 shape.
   - `elevation_mapping.py`: 생성자에서 `get_filter_torch`를 `try/except`로 감쌈 → torch 없으면 패스스루로 폴백. **나중에 torch 설치하면 자동으로 진짜 필터 복귀(코드 영구 훼손 없음).**
2. **의존성 정리**: `elevation_mapping_cupy/package.xml`에서 미사용 `<exec_depend>semantic_sensor</exec_depend>` 제거(코어 노드는 import 안 함, semantic 예제 런치만 참조).
3. **transforms3d 버그 수정**: 시스템 `transforms3d 0.3.x`가 numpy 1.24에서 제거된 `np.float` 사용 → pip `--user`로 `transforms3d==0.4.2` 업그레이드.
4. **빌드**: `colcon build --packages-select ros2_numpy elevation_map_msgs elevation_mapping_cupy` 성공.
5. **실행**:
   - 하위: `ros2 launch go2_traversability sensor_odom_bringup.launch.py`
   - EMC: `ros2 launch elevation_mapping_cupy elevation_mapping.launch.py robot_config:=go2/base.yaml`
6. **검증 결과** (`/elevation_mapping_node/elevation_map_raw`, ~4.8Hz, frame `camera_init`, 20×20m @0.1):
   - elevation: 실제 높이값(min −1.21 / max 2.15 / mean 0.16 m), 정지 상태라 관측률 ~6.7%(이동 시 증가)
   - traversability: 전부 1.000(패스스루 스텁 정상)
   - variance: 관측셀 0.003 / 미관측 1000(정상)

### 결과물/상태
- 발행 토픽: `/elevation_mapping_node/elevation_map_raw`, `/elevation_mapping_node/elevation_map_filter` (grid_map_msgs/GridMap)
- RViz 확인(디스플레이 있는 환경): `... elevation_mapping.launch.py robot_config:=go2/base.yaml launch_rviz:=true` (grid_map_rviz_plugin로 elevation 레이어 표시)

## 7단계 — 통합 launch + RViz (시각화 일원화) ✅
**문제**: 백그라운드로 띄운 노드(기본 FastDDS)와 사용자 터미널 RViz가 서로 토픽이 안 보임.
**원인**: go2의 `src/unitree_ros2/setup*.sh`가 `RMW_IMPLEMENTATION=rmw_cyclonedds_cpp`를 export → 미들웨어(RMW) 불일치 시 통신 불가.
**해결**: 노드 + RViz를 **하나의 launch로 같은 환경에서** 기동 → RMW 항상 일치.
- 신규: `go2_traversability/launch/full_elevation.launch.py`
  - sensor_odom_bringup(Ouster+FAST_LIO+bridge TF) → 10초 뒤 EMC → RViz(`config/elevation.rviz`)
  - 인자: `use_rviz:=true|false` (기본 true)  ※아래 7-1 버그수정 참조
- RViz config: `go2_traversability/config/elevation.rviz` (Fixed Frame `camera_init`, GridMap=elevation 무지개, Ouster 포인트클라우드는 기본 off).
- 헤드리스 검증: 4개 노드 기동 + elevation_map 5.36Hz, 에러 없음 확인.

### ▶ 사용자 실행 방법 (본인 터미널, 디스플레이 필요)
```bash
cd ~/go2_ws
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 launch go2_traversability full_elevation.launch.py
```
- RViz 창은 바로 뜨지만, FAST_LIO 초기화 + EMC 시작(10초)까지 **15~20초**는 빈 화면일 수 있음(정상).
- 종료: 그 터미널에서 Ctrl+C.
- 주의: 같은 터미널에서 unitree 셋업(CycloneDDS)을 추가로 source하지 말 것(혼선 방지). 순수 ROS 환경이면 됨.

## 7-1단계 — RViz가 안 뜨던 버그 수정 (launch 인자 이름 충돌) ✅
**증상**: `full_elevation.launch.py` 실행 시 다른 노드는 다 뜨는데 **RViz만 조용히 안 뜸**(에러도 없음, launch.log에 rviz2 spawn 자체가 없음).
**진단 과정**:
- 격리 테스트(rviz2 노드만) → 정상 spawn. 구조 테스트(더미 include+timer+rviz) → 정상 spawn.
- 충돌 재현 테스트 → 부모가 `rviz`(기본 true) 선언 + 하위 include에 `rviz:=false` 전달 시, 부모의 `IfCondition(LaunchConfiguration('rviz'))` 노드가 **안 뜸** → 원인 확정.
**원인**: ROS2 launch는 LaunchConfiguration이 include 경계에서 새는 경우가 있음. full_elevation이 `rviz` 인자를 선언했는데, 포함된 **FAST_LIO launch도 `rviz` 인자를 선언**하고 bringup이 거기에 `rviz:=false`를 넘기면서, 그 `false`가 전역 `rviz`로 새어 들어와 우리 RViz 조건을 꺼버림.
**수정**: full_elevation의 최상위 토글을 `rviz` → **`use_rviz`**로 개명(FAST_LIO의 `rviz`와 이름 분리). 프록시 테스트로 수정 후 정상 spawn 확인.
**교훈**: 다른 launch를 include할 때, 그 launch가 쓰는 인자명과 **같은 이름의 인자를 부모에서 쓰지 말 것**(특히 include에 그 인자를 넘길 때).

### ▶ 실행 (수정 후, 검증됨)
```bash
ros2 launch go2_traversability full_elevation.launch.py            # RViz 포함 (기본)
ros2 launch go2_traversability full_elevation.launch.py use_rviz:=false   # RViz 없이
```

### 다음 할 일 (2.5D 잘 되는 것 확인 후)
- [ ] (원하면) 로봇 이동시키며 맵 누적/품질 확인, 파라미터 튜닝(map_length/resolution/노이즈)
- [ ] traversability 실제화: JetPack6 CUDA torch 확보·설치 → 스텁 자동 해제 (또는 grid_map_filters 기하학 traversability)
- [ ] GridMap → OccupancyGrid 변환 노드
- [ ] Nav2 local costmap + controller



# 3d맵핑에서 3d포인트 클라우드 데이터 삭제한 오도메트리만을 시각화
ros2 launch go2_traversability fastlio_odom_test.launch.py

## 8단계 — 대안 SLAM: LIO-SAM 테스트 셋업 ✅
**배경**: FAST_LIO odometry가 의심되어, 비교용으로 LIO-SAM을 테스트하기로 함.
- GTSAM 이미 설치돼 있어(`ros-humble-gtsam 4.2.0`) 셋업 수월.
- clone: `src/LIO-SAM` (TixiaoShan, **ros2 브랜치**). 빌드 성공(`lio_sam`, ~2.5분).
- 이 ros2 브랜치는 `imageProjection.cpp`에서 IMU orientation 사용이 주석처리됨 → **6축 Ouster IMU에 맞게 수정된 버전**(다행).
- **params.yaml 수정** (`src/LIO-SAM/config/params.yaml`):
  - `pointCloudTopic: /ouster/points`, `imuTopic: /ouster/imu`
  - `Horizon_SCAN: 1024` (Ouster 1024x10 모드)
  - `extrinsicRot`/`extrinsicRPY` → **identity** (Ouster os_imu와 os_sensor는 회전 동일; 기본값은 Velodyne+Microstrain용이라 틀림)
- 테스트 launch 신규: `go2_traversability/launch/liosam_odom_test.launch.py` (Ouster + LIO-SAM + 자체 RViz).
- **솔직한 주의**: LIO-SAM도 IMU-LiDAR extrinsic·IMU 품질·시간동기 공유 → FAST_LIO 불량 원인이 그쪽이면 비슷하게 실패 가능. 비교 실험 목적.

### ▶ 실행
```bash
ros2 launch go2_traversability liosam_odom_test.launch.py
```

## 9단계 — go2_slam_2d_3d(felixokolo) 기반 LIO-SAM ✅ (작동 확인)
**배경**: TixiaoShan LIO-SAM 대신, 사용자가 지정한 https://github.com/felixokolo/go2_slam_2d_3d 의 LIO-SAM으로 교체 테스트. 기존 `lio_sam`과 구분되게 구성.
- clone: `src/go2_slam_2d_3d` (submodule Hesai/odom_to_tf/pointcloud_to_laserscan는 미수신=빈 폴더, LIO-SAM엔 불필요).
- 이 repo의 `LIO-SAM-ros2`는 robot_state_publisher(xacro)·imuPreintegration이 **주석 처리**된 버전 → xacro 문제·TF extrapolation 회피.
- **패키지 rename**: `lio_sam` → **`lio_sam_go2`** (package.xml/CMakeLists project/3개 cpp의 `lio_sam::msg|srv` 네임스페이스). 기존 TixiaoShan `lio_sam`과 **충돌 없이 공존**.
- **빌드 수정**: CMakeLists에 누락된 `find_package(pcl_conversions)` + ament_target_dependencies 추가 (Foxy→Humble 차이).
- **Ouster config** 신규: `config/params_ouster.yaml` (`/ouster/points`, `/ouster/imu`, sensor ouster, N_SCAN 64, Horizon_SCAN 1024, extrinsic identity, savePCD false).
- **dense-cloud 패치**: `imageProjection.cpp:267`에서 Ouster의 비-dense(NaN) 클라우드에 shutdown 대신 `pcl::removeNaNFromPointCloud` 적용 (안 그러면 즉시 종료).
- 테스트 launch 신규: `go2_traversability/launch/liosam_go2_test.launch.py` (Ouster + map→odom + URDF-identity TF들 + 3노드 + RViz).
- **검증**: imageProjection 생존, registered cloud 3.9Hz, odometry 발행 확인 ✅.
- 주의: 이 fork의 `rviz2.rviz`는 Hesai/Foxy용이라 RViz Fixed Frame을 `map`/`odom`으로 맞춰야 할 수 있음.

### ▶ 실행 (기존 lio_sam과 구분됨)
```bash
ros2 launch go2_traversability liosam_go2_test.launch.py     # felixokolo fork (lio_sam_go2)
ros2 launch go2_traversability liosam_odom_test.launch.py    # TixiaoShan (lio_sam)
```

### ★ 결론 (SLAM 비교)
3종(FAST_LIO / TixiaoShan LIO-SAM / **go2_slam_2d_3d fork = lio_sam_go2**) 중
**`lio_sam_go2`가 odometry/맵 성능이 가장 좋음** → 이걸 elevation 파이프라인의 자세 소스로 채택.

### ⚠️ 알려진 이슈
- SLAM 노드들이 Ctrl+C(SIGINT)에 **완전히 안 죽고 orphan**으로 남음(특히 mapOptimization). 그 orphan이 누적 맵을 계속 발행해서, 다음 launch 때 "이전 맵이 불려오는" 것처럼 보임.
  - 재launch 전 정리: `pkill -9 -f lio_sam_go2_ ; pkill -9 -f os_driver ; pkill -9 -f static_transform_publisher`


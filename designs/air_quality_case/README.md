# ESPHome 거실 공기질 센서 케이스 설계

이 설계는 현재 조립된 다음 부품을 기준으로 한 초안이다.

- ESP8266 NodeMCU v2
- MH-Z19 CO2 센서
- SDS011 미세먼지 센서
- DHT11 온습도 센서

## 설계 방향

사진 기준으로 SDS011이 가장 큰 부품이고 자체 팬을 가지고 있으므로, SDS011을 케이스의 기준 부품으로 배치한다. NodeMCU, MH-Z19, DHT11은 SDS011 주변에 분산 배치하되, DHT11은 NodeMCU 발열 영향을 덜 받도록 케이스 측면 가까이에 둔다.

추천 형태는 세로 타워형보다 낮은 데스크탑형이다.

- 외형: 약 130 x 105 x 42 mm
- 구조: 하부 트레이 + 상부 커버
- 전면: SDS011 흡기용 원형 타공
- 측면: MH-Z19와 DHT11 주변 슬릿 환기구
- 후면: USB 케이블 출구
- 내부: SDS011 받침, NodeMCU 받침, 케이블 여유 공간

## 내부 배치

```text
상단에서 본 배치

┌──────────────────────────────────────┐
│ MH-Z19            NodeMCU            │
│ 측면 슬릿         USB 후면 출구       │
│                                      │
│ ┌──────────────────────────────┐     │
│ │ SDS011                       │     │
│ │ 전면 원형 타공과 맞춤         │     │
│ └──────────────────────────────┘     │
│ DHT11 측면 슬릿                      │
└──────────────────────────────────────┘
```

## 주의점

- SDS011 팬 흡기구 앞에는 충분한 타공을 둔다.
- SDS011 배기 방향을 완전히 막지 않는다.
- MH-Z19는 SDS011 팬 바람이 직접 강하게 지나가는 위치를 피한다.
- DHT11은 ESP8266과 전원부에서 떨어뜨린다.
- 처음 출력할 때는 PLA로 0.2 mm 레이어, 15~20% infill 정도가 적당하다.
- 실제 부품 고정 전에는 `test_fit` 값을 `true`로 바꿔 바닥 트레이만 출력해 맞춰보는 것이 좋다.

## 파일

- `air_quality_case.scad`: OpenSCAD 파라메트릭 모델
- `generate_step.py`: CadQuery 기반 STEP 생성 스크립트
- `air_quality_case_base.stp`: 하부 트레이 STEP 파일
- `air_quality_case_lid.stp`: 상부 커버 STEP 파일
- `air_quality_case_assembly.stp`: 하부 트레이와 상부 커버를 나란히 둔 확인용 STEP 파일

## STEP 파일 다시 생성

CadQuery가 설치된 Python 환경에서 다음 명령을 실행한다.

```bash
python designs/air_quality_case/generate_step.py
```

현재 Mac에서는 작업용 가상환경 `.venv-cad/`에 CadQuery를 설치해 생성했다. 이 폴더는 로컬 도구이므로 Git에 포함하지 않는다.

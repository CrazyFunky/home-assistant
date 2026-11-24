# 장치와 공간

이 문서는 집의 물리적 구조, 주요 장치, Home Assistant 엔티티를 기록한다.

시스템이 확장될수록 이 파일도 함께 갱신한다.

## 공간

방과 공간을 여기에 추가한다.

| 공간 | 목적 | 메모 |
| --- | --- | --- |
| TBD | TBD | TBD |

## 핵심 시스템

| 시스템 | 위치 | 메모 |
| --- | --- | --- |
| 유/무선 라우터 | 네트워크 경계 | 공인 인터넷을 집 LAN과 Wi-Fi에 연결 |
| 미니 PC | TBD | Home Assistant와 MCP 서비스를 실행 |
| Home Assistant | 미니 PC | IoT 상태와 자동화의 중심 엔진 |
| MCP 서버 | 미니 PC | Codex의 실시간 접근 계층 |
| Zigbee 안테나 | Home Assistant 서버 | 물리적 Zigbee 무선 경로 제공 |
| Zigbee2MQTT | Home Assistant 서버 | Zigbee 장치를 MQTT/Home Assistant로 연결 |
| Nginx Proxy Manager | Home Assistant 환경 | 외부 DNS 기반 HTTPS 접근을 설정된 내부 서비스로 라우팅 |
| NAS 서버 | 집 LAN | 라우터 뒤에 연결된 저장소/서버 장치 |
| Matterbridge | 미니 PC / Home Assistant 환경 | 선택된 Home Assistant 장치를 Google Home에 연결 |
| Google Home | 클라우드 / Google Home 앱 | 가족 구성원의 음성 제어 표면 |
| Google 스피커 | 각 방 | Google Home 음성 명령 진입점 |

## 장치 인벤토리

| 장치 | 공간 | Home Assistant 엔티티 | 목적 | 메모 |
| --- | --- | --- | --- | --- |
| TBD | TBD | TBD | TBD | TBD |

## 이름 규칙

- 안정적이고 사람이 이해하기 쉬운 엔티티 이름을 우선한다.
- Home Assistant, 문서, 대시보드에서 공간 이름을 일관되게 유지한다.
- 자동화가 불명확하거나 임시적인 이름에 의존하지 않게 한다.
- 엔티티 이름을 바꾸기 전에는 해당 엔티티를 참조하는 자동화, 스크립트, 대시보드, 헬퍼, 문서를 확인한다.

## 장치 메모

장치별 특이사항, 배터리 동작, 보정 메모, 알려진 문제를 이곳에 기록한다.

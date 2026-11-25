# 집 운영 Codex 가이드

이 저장소는 우리 집 어시스턴트 시스템을 위한 운영 기억이자 작업 공간이다.

## 역할

Codex는 단순히 Home Assistant 설정을 돕는 도구가 아니라, 집 전체 운영을 돕는 비서로 동작한다.

이 비서는 다음을 관리하는 데 도움을 준다.

- Home Assistant 설정, 자동화, 스크립트, 장면, 헬퍼, 대시보드
- IoT 장치 상태, 이름, 구성, 제어 전략
- 루틴, 청소, 장보기, 유지보수, 알림, 집안 의사결정 같은 일상 운영
- 다른 컴퓨터에서도 같은 비서 역할을 이어갈 수 있게 하는 문서

## 운영 원칙

- 실시간 집 제어의 기준은 미니 PC로 본다.
- 지속적으로 남겨야 하는 맥락, 규칙, 결정, 설정 절차의 기준은 이 저장소로 본다.
- 중요한 결정은 채팅 기록에만 의존하지 말고 Markdown 파일에 남긴다.
- 가능하면 Home Assistant 자동화는 `device_id`보다 엔티티 기반 설정을 우선한다.
- 자동화, 대시보드, 스크립트, 헬퍼 정의를 바꾸기 전에는 기존 프로젝트 파일을 먼저 읽는다.
- 커밋되는 파일에는 비밀값, 접근 토큰, 비밀번호, 정확한 사설 주소, API 키를 저장하지 않는다.
- Home Assistant 동작을 수정할 때는 작고 되돌릴 수 있게 변경하고 문서화한다.
- 실제 장치 상태가 확실하지 않으면 추측하지 말고 Home Assistant 또는 MCP 데이터를 확인한다.

## 새 Codex 세션 시작 절차

1. 이 파일을 먼저 읽는다.
2. `HOUSE.md`를 읽고 집 운영 철학을 이해한다.
3. `MCP.md`를 읽고 실시간 집 시스템에 접근하는 방식을 이해한다.
4. 장치, 방, 엔티티를 추정하기 전에 `DEVICES.md`를 읽는다.
5. 집안 루틴을 설계하기 전에 `OPERATIONS.md`를 읽는다.
6. 최근 결정과 과거 맥락을 확인하기 위해 `HOUSE_LOG.md`를 읽는다.
7. Home Assistant 대시보드를 확인하거나 변경하기 전에 `DASHBOARDS.md`를 읽는다.
8. 파일 기반 Home Assistant 설정 동기화나 YAML 수정을 계획하기 전에 `GITOPS.md`를 읽는다.
1. Read this file first.
2. Read `HOUSE.md` to understand the home's operating philosophy.
3. Read `MCP.md` to understand how live home systems are accessed.
4. Read `DEVICES.md` before making device, room, or entity assumptions.
5. Read `OPERATIONS.md` before designing household routines.
6. Read `HOUSE_LOG.md` for recent decisions and historical context.
7. Read `DASHBOARDS.md` before inspecting or changing Home Assistant dashboards.
8. Read `GITOPS.md` before planning file-based Home Assistant configuration sync or YAML edits.
9. Read `HOME_ASSISTANT_INSTALL_GUIDE.md` before planning a new Home Assistant host or reinstall.

## 편집 규칙

- 사용자의 기존 변경을 보존한다.
- 관련 없는 Home Assistant 설정을 다시 쓰지 않는다.
- 추적되는 파일에 비밀값을 직접 넣지 않는다.
- 의미 있는 운영 결정은 `HOUSE_LOG.md`에 기록한다.
- 새 PC 설정 단계가 새로 확인되면 `SETUP_NEW_PC.md`를 업데이트한다.
- 모든 작은 변경마다 커밋하지 않는다. 일상적인 문서/정리 변경은 로컬에 모아 두고, 사용자가 즉시 커밋을 명시적으로 요청하지 않는 한 주 1회 요약 커밋으로 반영한다.

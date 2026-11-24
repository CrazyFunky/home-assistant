# MCP와 실시간 집 접근

이 문서는 Codex가 실시간 집 시스템에 접근하는 방식을 설명한다.

## 기준 시스템

실시간 집 제어의 기준은 미니 PC다.

미니 PC 또는 그 주변에서 동작할 것으로 기대되는 서비스는 다음과 같다.

- Home Assistant
- Home Assistant와 집안 도구를 위한 MCP 서버
- IoT 브리지와 연동 서비스
- 선택된 Home Assistant 장치를 Google Home에 노출하기 위한 Matterbridge
- 집 운영에 필요한 보조 서비스

## 홈 네트워크 구조

현재 집 네트워크는 아래처럼 구성되어 있다.

```text
공인 인터넷
-> 유/무선 라우터
-> 유선 및 무선 집안 장치
   -> Home Assistant 서버
      -> Zigbee 안테나
      -> Zigbee2MQTT 서버
      -> Nginx Proxy Manager
      -> Matterbridge
      -> MCP 접근 계층
   -> NAS 서버
   -> 기타 유선/무선 장치
```

라우터는 공인 인터넷과 집 LAN 사이의 경계다. Home Assistant, NAS, 기타 집안 장치는 라우터 뒤에서 유선 또는 무선 네트워크로 연결된다.

Home Assistant에는 Zigbee 안테나가 연결되어 있고 Zigbee2MQTT가 실행된다. Zigbee 장치는 물리적 무선 경로가 Zigbee2MQTT를 거치더라도 Home Assistant가 제어하는 장치 계층의 일부로 본다.

Nginx Proxy Manager는 Home Assistant 환경에 설치되어 있다. 외부 DNS 기반 접근은 먼저 Nginx Proxy Manager에 도달하고, Nginx Proxy Manager가 요청을 설정된 내부 서비스로 라우팅한다.

## 현재 원격 MCP 접근

현재 Codex에서 Home Assistant MCP로 접근하는 경로는 다음과 같다.

```text
외부 컴퓨터의 Codex
-> 외부 DNS 이름
-> Nginx Proxy Manager 리버스 프록시
-> Home Assistant MCP 서버
-> Home Assistant
```

이것이 현재 사용 중인 실시간 원격 접근 모델이다. 이 경로는 MCP를 위해 의도적으로 노출한 HTTPS 리버스 프록시 경로이며, 일반적인 LAN 접근 방식으로 취급하지 않는다.

이 경로의 보안 규칙은 다음과 같다.

- Samba, SSH, NAS, 라우터 관리자, 임의의 LAN 서비스를 같은 경로로 노출하지 않는다.
- 정확한 DNS 이름, MCP 비밀 경로, bearer 토큰, Home Assistant 토큰은 로컬 전용 ignored 파일에 둔다.
- 가능하면 좁은 MCP 엔드포인트와 최소 권한 Home Assistant 토큰을 사용한다.
- 나중에 VPN 또는 AI 게이트웨이가 추가되면, 그것이 현재 NPM 리버스 프록시 경로를 대체하는지 보완하는지 문서화한다.

## 음성 제어 경로

현재 음성 제어 경로는 다음과 같다.

```text
Home Assistant 장치
-> Matterbridge
-> Google Home
-> Google 스피커
-> 가족의 음성 명령
```

장치 상태와 자동화 동작의 기준은 계속 Home Assistant다. Matterbridge는 선택된 Home Assistant 장치를 Google Home에서 사용할 수 있게 해 주는 브리지이며, 가족 구성원은 Google 스피커를 통해 음성으로 장치를 제어한다.

음성 제어 문제를 확인할 때는 다음 순서로 점검한다.

1. 장치가 Home Assistant에서 직접 동작하는지 확인한다.
2. 장치가 Matterbridge를 통해 노출되어 있는지 확인한다.
3. 장치가 Google Home에 올바르게 표시되는지 확인한다.
4. 대상 Google 스피커 또는 음성 명령 경로가 동작하는지 확인한다.

## 접근 모델

다른 컴퓨터는 별도의 집 제어 권한자가 되어서는 안 된다.

다른 컴퓨터는 접근 단말로 동작해야 한다.

```text
다른 PC의 Codex
-> 이 저장소를 연다
-> 미니 PC에 안전하게 연결한다
-> MCP/Home Assistant를 사용해 실시간 상태와 동작을 처리한다
```

## 안전한 원격 접근

원격 연결에는 다음과 같은 안전한 사설 접근 방식을 사용한다.

- Tailscale
- ZeroTier
- WireGuard
- 그 밖의 신뢰할 수 있는 VPN

의도적으로 검토된 보안 설계가 없다면 Home Assistant 또는 MCP 서버를 공인 인터넷에 직접 노출하지 않는다.

## 비밀값

다음은 커밋하지 않는다.

- 접근 토큰
- API 키
- 비밀번호
- 사설 터널 키
- 정확한 민감 주소

다음과 같은 로컬 전용 파일이나 저장소를 사용한다.

- `.env`
- `secrets.yaml`
- Codex 로컬 설정
- 운영체제 키체인 또는 비밀번호 관리자

추적되는 파일에는 자리표시자만 예시로 둔다.

## 연결 체크리스트

새 컴퓨터를 설정할 때:

1. 신뢰할 수 있는 홈 네트워크 또는 VPN에 연결한다.
2. 미니 PC에 접근 가능한지 확인한다.
3. Home Assistant에 접근 가능한지 확인한다.
4. MCP 서버 엔드포인트에 접근 가능한지 확인한다.
5. 로컬 비밀값 또는 토큰을 설정한다.
6. 이 저장소에서 Codex를 시작한다.
7. Codex에게 `AGENTS.md`를 읽게 한다.

## 로컬 Codex MCP 설정

이 저장소는 프로젝트 범위의 로컬 Codex MCP 설정 파일 `.codex/config.toml`을 사용할 수 있다.

이 파일에는 비공개 Home Assistant MCP 엔드포인트 정보가 들어갈 수 있으므로 반드시 로컬 전용으로 유지한다. Git에서 무시되며 커밋하지 않아야 한다.

로컬 환경 힌트는 `.env`에도 저장될 수 있고, 이 파일 역시 Git에서 무시된다.

## 접근 프로필

각 컴퓨터는 네트워크 위치에 맞는 접근 프로필을 선택해야 한다.

- `local`: 집 안 네트워크에 있을 때 사설 LAN Home Assistant IP와 사설 LAN MCP 엔드포인트를 사용한다.
- `remote`: 집 밖에 있을 때 외부 DNS/HTTPS Home Assistant 주소와 원격 MCP 엔드포인트를 사용한다.

Home Assistant는 현재 두 가지 방식으로 접근할 수 있다.

- 집 안 네트워크: 사설 IP 주소
- 집 밖 네트워크: 외부 DNS 이름

집에 있을 때는 불필요한 외부 라우팅을 피하기 위해 로컬 IP 경로를 우선한다. 집 밖에 있거나 사설 LAN 주소에 접근할 수 없는 네트워크에서는 DNS 경로를 사용한다.

정확한 URL, bearer 토큰, MCP 비밀 경로는 ignored 로컬 파일에만 둔다.

- `.env`: `HOME_ASSISTANT_URL`, `HOME_ASSISTANT_LOCAL_URL`, `HOME_ASSISTANT_REMOTE_URL`, `MCP_HOME_SERVER_URL`, `MCP_HOME_LOCAL_SERVER_URL`, `MCP_HOME_REMOTE_SERVER_URL` 같은 로컬 환경 힌트
- `.codex/config.toml`: 프로젝트 범위의 Codex MCP 서버 설정

원격 MCP 접근을 설정할 때는 필요한 MCP 비밀 경로를 ignored 로컬 URL에 포함한다. 그 경로를 커밋하지 않는다.

## 미정 항목

- 미니 PC 호스트 이름 또는 사설 VPN 이름 문서화
- MCP 서버 이름과 목적 문서화
- 확인된 로컬 설정 명령 문서화
- 확인된 상태 점검 명령 문서화

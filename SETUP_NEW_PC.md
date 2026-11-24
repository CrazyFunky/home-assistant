# 새 장치 설정

다른 장치에서 같은 집 어시스턴트 환경을 이어가기 위한 체크리스트다.

## 목표

설정이 끝난 새 장치는 다음을 할 수 있어야 한다.

- 이 저장소 열기
- 집 운영 규칙 이해하기
- 미니 PC에 안전하게 연결하기
- MCP/Home Assistant를 사용해 실시간 상태와 동작 처리하기
- 처음 사용하던 Mac에 의존하지 않고 작업 이어가기

정확한 설정 방식은 플랫폼마다 다르다.

- macOS와 Windows는 전체 작업 환경이다.
- 스마트폰은 검토, 긴급 수정, Home Assistant 제어, 이어가기 프롬프트를 위한 가벼운 접근 단말이다.

## 준비 사항

- Codex 설치
- Git 설치
- 원격 저장소 접근 권한
- 안전한 홈 네트워크 또는 VPN 접근
- 비밀번호 관리자나 신뢰할 수 있는 로컬 출처에서 필요한 비밀값 또는 토큰 확인 가능

## GitHub 접근

저장소:

```text
https://github.com/CrazyFunky/home-assistant.git
```

GitHub 토큰을 Codex에게 주지 말고, 이 저장소에 커밋하지 않는다.

각 장치는 운영체제 자격 증명 관리자, Git Credential Manager, 신뢰할 수 있는 비밀번호 관리자에 자체 GitHub 자격 증명을 로컬로 저장해야 한다.

HTTPS Git 접근에서는 GitHub 계정 비밀번호를 사용할 수 없다. 대신 Personal Access Token을 사용한다.

권장 토큰 규칙:

- 가능하면 토큰 범위를 이 저장소로만 제한한다.
- `Contents: Read and write` 권한을 부여한다.
- 토큰은 해당 장치에 로컬로 저장한다.
- 토큰을 채팅에 붙여넣지 않는다.
- 장치를 잃어버렸거나 더 이상 신뢰하지 않는 경우 토큰을 교체하거나 폐기한다.

## macOS 설정

1. Codex를 설치한다.
2. Git을 설치한다. Xcode Command Line Tools 또는 Homebrew Git 모두 가능하다.
3. 홈 VPN 또는 신뢰할 수 있는 네트워크에 연결한다.
4. 이 저장소를 클론한다.

```bash
git clone https://github.com/CrazyFunky/home-assistant.git
cd home-assistant
```

5. Codex에서 저장소를 연다.
6. Keychain, 비밀번호 관리자, `.env`, 기타 로컬 전용 파일에 로컬 비밀값과 토큰을 설정한다.
7. 미니 PC로 연결되는 MCP 연결을 설정한다.
8. Home Assistant에 접근 가능한지 확인한다.
9. Codex에게 `AGENTS.md`를 읽게 한다.
10. Codex에게 `HOUSE_LOG.md` 기준으로 현재 상태를 요약하게 한다.

## Windows 설정

1. Codex를 설치한다.
2. Git for Windows를 설치한다.
3. Git 설치 과정에서 Git Credential Manager가 활성화되어 있는지 확인한다.
4. 홈 VPN 또는 신뢰할 수 있는 네트워크에 연결한다.
5. PowerShell 또는 Windows Terminal을 연다.
6. 이 저장소를 클론한다.

```powershell
git clone https://github.com/CrazyFunky/home-assistant.git
cd home-assistant
```

7. Codex에서 저장소를 연다.
8. Windows Credential Manager, 비밀번호 관리자, `.env`, 기타 로컬 전용 파일에 로컬 비밀값과 토큰을 설정한다.
9. 미니 PC로 연결되는 MCP 연결을 설정한다.
10. Home Assistant에 접근 가능한지 확인한다.
11. Codex에게 `AGENTS.md`를 읽게 한다.
12. Codex에게 `HOUSE_LOG.md` 기준으로 현재 상태를 요약하게 한다.

### Windows 참고 사항

- Codex나 PowerShell이 이미 열린 상태에서 Git을 설치했다면, 업데이트된 `PATH`가 로드되도록 터미널 또는 Codex를 다시 시작한다.
- 설치 직후 현재 세션에서 `git`을 찾지 못해도 보통 `C:\Program Files\Git\cmd\git.exe`에서 Git을 확인할 수 있다.
- GitHub 자격 증명은 Git Credential Manager 또는 Windows Credential Manager에 보관한다. 토큰을 Codex 채팅에 붙여넣거나 저장소에 커밋하지 않는다.
- 이 저장소는 지속 맥락 저장소로 사용하고, 실시간 Home Assistant와 MCP 상태는 미니 PC를 기준으로 사용한다.

## 스마트폰 설정

스마트폰은 대규모 Home Assistant 수정이나 저장소 편집을 위한 주 작업 환경이 아니라, 가벼운 접근 단말로 다룬다.

스마트폰은 다음 용도로 사용한다.

- 저장소 읽기
- `HOUSE_LOG.md` 확인
- 집 상태나 다음 작업 질문
- 작은 변경 검토 또는 승인
- Home Assistant 접근
- 긴급 상황 또는 책상 밖에서의 작업

### Android

1. Home Assistant 앱을 설치한다.
2. Tailscale, ZeroTier, WireGuard 같은 홈 접근용 VPN 앱을 설치한다.
3. GitHub Mobile을 설치하거나 브라우저에서 GitHub를 사용한다.
4. GitHub에 `CrazyFunky` 계정으로 로그인한다.
5. `https://github.com/CrazyFunky/home-assistant`를 연다.
6. `AGENTS.md`, `SETUP_NEW_PC.md`, `HOUSE_LOG.md`를 읽을 수 있는지 확인한다.
7. 저장소에 접근할 수 있는 모바일 Codex 또는 ChatGPT 환경을 사용한다면 아래 이어가기 프롬프트로 시작한다.

### iOS

1. Home Assistant 앱을 설치한다.
2. Tailscale, ZeroTier, WireGuard 같은 홈 접근용 VPN 앱을 설치한다.
3. GitHub Mobile을 설치하거나 Safari에서 GitHub를 사용한다.
4. GitHub에 `CrazyFunky` 계정으로 로그인한다.
5. `https://github.com/CrazyFunky/home-assistant`를 연다.
6. `AGENTS.md`, `SETUP_NEW_PC.md`, `HOUSE_LOG.md`를 읽을 수 있는지 확인한다.
7. 저장소에 접근할 수 있는 모바일 Codex 또는 ChatGPT 환경을 사용한다면 아래 이어가기 프롬프트로 시작한다.

### 스마트폰 한계

- 광범위한 GitHub 토큰을 일반 텍스트 메모에 저장하지 않는다.
- 모바일에서는 읽기/검토를 우선하고, 커밋/푸시는 macOS 또는 Windows에서 진행한다.
- 모바일 토큰이 필요하면 저장소 범위로 제한하고 더 이상 필요하지 않을 때 폐기한다.
- 긴급 실시간 제어는 휴대폰에서 자동화 파일을 편집하기보다 VPN을 통해 Home Assistant 앱을 사용한다.

## Codex 첫 프롬프트

새 장치에서 저장소를 열었을 때 이 프롬프트를 사용한다.

```text
AGENTS.md를 먼저 읽고, HOUSE.md, MCP.md, DEVICES.md, OPERATIONS.md, HOUSE_LOG.md를 읽은 다음 우리 집 운영 비서 역할을 이어가.
```

새 세션이 최신 문서화된 맥락에서 이어져야 한다면 다음을 추가한다.

```text
HOUSE_LOG.md의 마지막 항목을 기준으로 현재 상태를 요약하고 다음에 해야 할 일을 제안해줘.
```

## 검증

다음을 확인한다.

- `AGENTS.md`를 읽을 수 있다.
- `HOUSE.md`를 읽을 수 있다.
- 미니 PC에 접근할 수 있다.
- 집 안 네트워크에서는 사설 IP로 Home Assistant에 접근할 수 있다.
- 집 밖 네트워크에서는 외부 DNS로 Home Assistant에 접근할 수 있다.
- MCP 도구를 사용할 수 있다.
- Git에 비밀값이 커밋되지 않았다.
- `git pull`이 동작한다.
- 로컬 인증 후 `git push`가 동작한다.

스마트폰에서는 최소한 다음을 확인한다.

- 안전한 네트워크 경로를 통해 Home Assistant 앱이 동작한다.
- GitHub 저장소를 읽을 수 있다.
- 비서에게 맥락 이어가기를 요청하기 전에 `HOUSE_LOG.md`를 확인할 수 있다.

## 필요할 수 있는 로컬 파일

다음 파일은 로컬에 있을 수 있지만 실제 비밀값이 들어간 상태로 커밋하면 안 된다.

- `.env`
- `secrets.yaml`
- 로컬 Codex 설정 파일
- VPN 설정
- SSH 키
- 로컬 자격 증명 관리자 또는 비밀번호 관리자에 저장된 GitHub Personal Access Token

## 문제가 생겼을 때

다음 순서로 확인한다.

1. VPN 또는 네트워크 연결
2. 미니 PC 전원과 네트워크 상태
3. Home Assistant 상태
4. MCP 서버 상태
5. 로컬 토큰 또는 비밀값 설정
6. Codex 프로젝트 설정
7. 플랫폼별 자격 증명 관리자 동작

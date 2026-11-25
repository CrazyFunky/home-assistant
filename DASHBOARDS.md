# 대시보드 관리

이 문서는 우리 집 Home Assistant 대시보드가 어떻게 구성되어 있고 어떻게 유지보수해야 하는지 기록한다.

## 현재 대시보드

현재 집에서는 같은 button-card 디자인 언어에서 파생된 태블릿용 대시보드 화면 두 개를 사용한다.

| 대시보드 | URL 경로 | 모드 | 목적 |
| --- | --- | --- | --- |
| 개요 | `lovelace` | YAML | `ui-lovelace.yaml`을 기반으로 하는 메인 태블릿 대시보드 |
| SweetHome | `lovelace-sweetkitchen` | Storage | 메인 대시보드에서 파생된 작은 태블릿용 대시보드 |

다른 대시보드도 있을 수 있지만, 이 두 개가 거실 태블릿용 주요 대시보드다.

## 디자인 관계

`ui-lovelace.yaml`은 기준 대시보드다.

`SweetHome`은 작은 화면용 파생 대시보드다. 전체 레이아웃과 button-card 동작은 유지하되, 작은 태블릿 화면에 맞게 카드 크기와 글자 크기를 줄였다.

알려진 차이는 다음과 같다.

| 설정 | `ui-lovelace.yaml` | `SweetHome` |
| --- | --- | --- |
| `custom_base_card` 높이 | `100px` | `80px` |
| 이름 글자 크기 | `0.8em` | `0.7em` |
| 상태 글자 크기 | `0.7em` | `0.6em` |
| 메인 아이콘 너비 | `2em` | `1.7em` |

## 템플릿 전략

대시보드는 `custom:button-card`를 기반으로 한다.

중요한 템플릿 그룹은 다음과 같다.
Shared button-card templates are kept under the dashboard folder:

```yaml
# /config/ui-lovelace.yaml
button_card_templates: !include dashboards/button_card_templates.yaml
```

For YAML dashboard files stored inside `/config/dashboards/`, use the dashboard file's own directory as the include base:

```yaml
# /config/dashboards/sweethome.yaml
button_card_templates: !include button_card_templates.yaml
```

Important template groups:

- `custom_base_card`: 기본 레이아웃, 카드 높이, grid 영역, 공통 애니메이션 훅
- `custom_light_card`: 조명 상태, 색상, 배경, 아이콘 애니메이션
- `custom_switch_card`: 스위치 상태, 선택적 전력 표시, 아이콘 애니메이션
- `custom_media_card`: 미디어 상태, 재생 표시, 배경 이미지 처리
- `custom_climate_card`: 냉난방 상태와 냉방/팬 표시
- `custom_cover_card`: 커튼, 블라인드, 커버 표시
- `custom_vacuum_card`: 로봇청소기 상태 표시
- `custom_floor_card`: 평면도 버튼 상태 표시
- 온도, 습도, 전력, 신호, 슬라이더, 옵션 필드 표시 템플릿
- `custom_action`: 탭, 더블탭, 길게 누르기, 햅틱, 버튼 애니메이션 동작

`SweetHome`은 storage-mode이므로 `button_card_templates.yaml` 같은 YAML `!include` 파일을 편하게 공유하기 어렵다. 지금은 대시보드 모드를 유지하고, 즉시 변환하기보다 차이점을 이 문서에 기록한다.
Because `SweetHome` is storage-mode, it cannot conveniently share YAML `!include` files such as `dashboards/button_card_templates.yaml`. For now, keep the current dashboard modes and document differences here instead of converting dashboards immediately.

## File Organization Principle

Keep Home Assistant's default root-level files at `/config`, and place user-created supporting files in purpose-specific folders.

Root-level files that should normally stay in `/config`:

```text
configuration.yaml
automations.yaml
scripts.yaml
scenes.yaml
secrets.yaml
ui-lovelace.yaml
```

User-created supporting files should be grouped by purpose:

```text
dashboards/   # YAML dashboard files and dashboard-specific includes
include/      # package files loaded through homeassistant.packages
www/          # local frontend assets
themes/       # theme YAML files
```

This keeps a fresh Home Assistant install's expected files recognizable while making custom household configuration easier to review, sync, and restore.

## 유지보수 규칙

- `ui-lovelace.yaml`을 디자인 기준으로 본다.
- `SweetHome`은 별개의 대시보드가 아니라 작은 화면용 파생본으로 본다.
- 어느 대시보드를 바꾸든 먼저 `button_card_templates`를 확인한다.
- 변경이 다음 중 어디에 해당하는지 판단한다.
  - 두 대시보드에 모두 반영해야 하는 공통 동작
  - 화면 크기 때문에 다르게 유지해야 하는 동작
- Home Assistant `.storage` 파일을 직접 편집하지 않는다.
- storage-mode 대시보드는 Home Assistant 대시보드 API/MCP 도구로 수정한다.
- YAML-mode 대시보드는 관리되고 검증 가능한 경로를 통해 대시보드 YAML 파일을 직접 수정한다.
- 태블릿 사용성을 유지한다. 대상 태블릿 화면을 확인하지 않고 카드 높이, 글자 크기, 간격을 키우지 않는다.
- 작고 되돌릴 수 있는 대시보드 수정을 우선한다.

## 향후 개선 방향

장기적으로 가장 유지보수하기 쉬운 구조는 파생 대시보드를 YAML-mode로 전환하고 공통 파일을 공유하는 방식이다.

```yaml
button_card_templates: !include button_card_templates.yaml
views: !include sweethome/views.yaml
```

그 다음 작은 화면 차이는 아래처럼 명시적인 override 템플릿으로 처리할 수 있다.

```yaml
custom_base_card_small:
  template: custom_base_card
  styles:
    card:
      - height: 80px
```

이 전환은 가볍게 진행하지 않는다. 현재 태블릿 대시보드가 실제로 사용 중이므로 계획된 대시보드 마이그레이션으로 다룬다.

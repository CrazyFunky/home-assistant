# Home Assistant GitOps 계획

이 문서는 Git으로 동기화할 수 있는 범위와 필요한 접근 경로를 기록한다.

## 현재 확인 내용

현재 원격 Codex 접근 경로는 다음과 같다.

```text
Codex
-> 외부 DNS
-> Nginx Proxy Manager
-> Home Assistant MCP 서버
-> Home Assistant API
```

이 경로는 API를 통해 여러 Home Assistant 설정 객체를 확인하고 수정할 수 있다. HA MCP Tools 통합을 등록한 뒤에는 MCP 서버의 allowlist 파일 도구를 통해 보호된 파일/YAML 작업도 수행할 수 있다.

## 현재 MCP/API로 접근 가능한 항목

현재 MCP 경로로 확인 가능한 항목은 다음과 같다.

| 영역 | 현재 상태 | GitOps 메모 |
| --- | --- | --- |
| 설치된 add-on | 접근 가능 | 인벤토리에는 유용하지만 전체 add-on 데이터 내보내기는 아님 |
| storage-mode 대시보드 | 접근 가능 | 대시보드 API로 가져오고 수정 가능 |
| YAML-mode 대시보드 등록 정보 | 일부 접근 가능 | 대시보드 메타데이터는 보이며, YAML 본문에는 allowlist 파일 도구가 필요 |
| 자동화 | HA 설정 객체로 접근 가능 | 객체 단위로 내보낼 수 있음 |
| 스크립트 | HA 설정 객체로 접근 가능 | 객체 단위로 내보낼 수 있음 |
| 장면 | 접근 가능, 현재 발견된 항목 없음 | 생성되면 객체 단위로 내보낼 수 있음 |
| 블루프린트 | 접근 가능, 현재 발견된 항목 없음 | 존재하면 내보낼 수 있음 |
| HACS 설치 메타데이터 | 접근 가능 | 인벤토리와 재설치 메모에 유용 |
| 통합 메타데이터 | 접근 가능 | 인벤토리에 유용하지만 비밀값/옵션은 커밋 금지 |
| 테마 | 테마 목록으로 접근 가능, 현재 발견된 항목 없음 | 테마 YAML 파일은 allowlist 파일/YAML 도구로 접근 가능 |
| 백업 | 백업 메타데이터로 접근 가능 | 전체 백업 tarball은 커밋 금지 |

확인된 현재 수량:

- 설치된 add-on: 12개, 모두 실행 중
- 자동화: 24개
- 스크립트: 24개
- 장면: 0개
- 자동화 블루프린트: 0개
- 스크립트 블루프린트: 0개
- 설치된 HACS 저장소: 13개
- 설치된 HACS Lovelace 카드: 4개
- 테마: 0개

## Home Assistant 백업 활용 가능성

Home Assistant snapshot 백업은 MCP로 접근 가능하다.

현재 확인된 백업 상태:

- 발견된 snapshot 백업: 14개
- 백업 주기는 월간으로 보임
- 목록에 있는 대부분의 백업은 Home Assistant 설정과 데이터베이스를 포함함
- 백업 크기는 대략 500-700 MB
- MCP 백업 도구로 복원 기능은 존재하지만, 복원은 복구 작업이며 Home Assistant를 재시작함

백업은 다음에 유용하다.

- 위험한 변경 전 복구 수단 확보
- 정기 HA 백업이 존재하는지 확인
- 잘못된 변경 후 전체 Home Assistant 설정 복원

백업이 기본 GitOps 배포 경로로 적합하지 않은 이유는 다음과 같다.

- 현재 MCP 백업 도구는 snapshot을 나열, 생성, 복원할 수 있지만, "파일 하나 추출" 또는 "수정한 백업 tarball 업로드" 같은 안전한 워크플로를 제공하지 않는다.
- snapshot 복원은 `ui-lovelace.yaml` 같은 단일 파일 변경보다 훨씬 넓고 파괴적이다.
- 백업에는 데이터베이스, 비밀값, add-on 데이터, 토큰, local key, 기타 개인 정보가 포함될 수 있다.
- 백업 복원은 관련 없는 런타임 변경을 덮어쓸 수 있고 Home Assistant 재시작이 필요할 수 있다.

대시보드 YAML이나 설정 YAML을 업데이트하는 일반적인 방법으로 백업 복원을 사용하지 않는다. 백업은 GitOps 또는 파일 동기화 워크플로 주변의 안전망으로 사용한다.

권장 패턴:

```text
1. 최근 HA 백업을 생성하거나 존재 여부를 확인한다.
2. Git, SSH, Samba, 또는 향후 파일 MCP 게이트웨이를 통해 안전한 YAML 파일을 동기화/수정한다.
3. Home Assistant 설정 검증을 실행한다.
4. 가능하면 영향을 받은 통합/대시보드만 reload한다.
5. 꼭 필요할 때만 재시작한다.
6. 복구가 필요할 때만 백업 복원을 사용한다.
```

## GitOps와 관련된 설치된 add-on

| Add-on | Slug | 용도 |
| --- | --- | --- |
| File editor | `core_configurator` | 브라우저 기반 수동 파일 편집 |
| Samba share | `core_samba` | 내부 LAN 파일 접근 |
| Terminal & SSH | `core_ssh` | 내부 LAN 쉘 접근 |
| Node-RED | `a0d7b954_nodered` | 플로우 로직과 데이터 변환 가능성 |
| ESPHome Device Builder | `5c53de3b_esphome` | ESPHome YAML 관리 |
| Zigbee2MQTT | `45df7312_zigbee2mqtt` | Zigbee 장치 브리지 |
| Nginx Proxy Manager | `a0d7b954_nginxproxymanager` | 외부 DNS 리버스 프록시 |
| Home Assistant MCP Server | `81f33d0f_ha_mcp` | 현재 Codex 원격 API 경로 |

add-on 옵션을 무턱대고 읽거나 커밋하지 않는다. 일부 add-on에는 토큰, 비밀번호, local key, 비공개 URL이 들어 있을 수 있다.

## MCP 파일시스템 접근

HA MCP Tools가 Home Assistant 통합으로 등록되어 있으므로 MCP 경로에는 보호된 파일 접근 권한이 있다.

현재 사용 가능한 파일 작업은 다음과 같다.

- `ha_read_file`
- `ha_list_files`
- `ha_write_file`
- `ha_delete_file`
- `ha_config_set_yaml`

이것은 제한 없는 shell/Samba 접근이 아니다. 통제된 수정을 위한 allowlist 기반 안전 점검 파일 경로다.

보호된 파일 경로로 접근 또는 수정이 확인된 항목:

| 파일 또는 디렉터리 | 중요한 이유 |
| --- | --- |
| `/config/ui-lovelace.yaml` | 메인 YAML-mode 대시보드 본문 |
| `/config/button_card_templates.yaml` | 공유 button-card 디자인 템플릿 |
| `/config/configuration.yaml` | 핵심 YAML 설정. 최상위 편집은 검증과 백업이 실행되도록 `ha_config_set_yaml` 사용 권장 |
| `/config/automations.yaml` | YAML 자동화 파일을 사용하는 경우 |
| `/config/scripts.yaml` | YAML 스크립트 파일을 사용하는 경우 |
| `/config/scenes.yaml` | YAML 장면 파일을 사용하는 경우 |
| `/config/include/` | `homeassistant.packages: !include_dir_named include`로 로드되는 package 파일, recorder 설정 포함 |
| `/config/www/` | 로컬 대시보드 asset과 커스텀 frontend 파일 |
| `/config/themes/` | 테마 YAML 파일 |
| `/config/ui-lovelace.yaml` | Main YAML-mode dashboard body |
| `/config/dashboards/button_card_templates.yaml` | Shared button-card design templates |
| `/config/configuration.yaml` | Core YAML configuration; top-level edits should use `ha_config_set_yaml` so validation and backups run |
| `/config/automations.yaml` | YAML automation file if used |
| `/config/scripts.yaml` | YAML script file if used |
| `/config/scenes.yaml` | YAML scene file if used |
| `/config/include/` | Package files loaded through `homeassistant.packages: !include_dir_named include`, including recorder configuration |
| `/config/dashboards/` | YAML dashboard files and dashboard-specific includes |
| `/config/www/` | Local dashboard assets and custom frontend files |
| `/config/themes/` | Theme YAML files |

다음 영역은 여전히 신중하게 수동 검토해야 한다.

| 파일 또는 디렉터리 | 중요한 이유 |
| --- | --- |
| `/config/custom_components/` | 커스텀 통합. 보통 전체 커밋보다 HACS 메타데이터 추적이 더 적합 |
| `/config/esphome/` | ESPHome 장치 YAML 파일이 그곳에 있을 경우 |
| `/addon_configs/` | HAOS 레이아웃에 따라 Node-RED 또는 Zigbee2MQTT 설정 같은 add-on 데이터 |

`secrets.yaml`, 토큰, 비밀번호, 데이터베이스 파일, 개인 키는 절대 커밋하지 않는다.

## 권장 GitOps 범위

보수적인 GitOps 범위에서 시작한다.

```text
/config/ui-lovelace.yaml
/config/dashboards/
/config/configuration.yaml
/config/automations.yaml
/config/scripts.yaml
/config/scenes.yaml
/config/include/
/config/www/lovelace/
/config/themes/
/config/esphome/
```

`/addon_configs/`는 실제 디렉터리 구조를 확인하고 비밀값을 제외한 뒤에만 추가한다.

## 권장 제외 항목

절대 커밋하지 않는다.

```text
secrets.yaml
service_account.json
secrets/
.storage/
home-assistant_v2.db*
*.log
*.key
*.pem
*.crt
*.token
*.db
*.sqlite
deps/
tts/
backups/
```

주의가 필요한 항목:

```text
custom_components/
www/
addon_configs/
esphome/
```

이 항목들은 통합에 따라 생성 파일, vendor 다운로드, 자격 증명을 포함할 수 있다.

## 다음 단계

Codex가 `ui-lovelace.yaml` 또는 `configuration.yaml` 같은 알려진 YAML 파일을 업데이트해야 할 때는 보호된 MCP 파일 도구를 사용해 좁은 원격 수정을 수행한다.

지속적인 GitOps를 위해서는 Git을 이력과 검토의 기준으로 유지한다.

1. 위험한 파일 변경 전 최근 HA 백업을 생성하거나 확인한다.
2. 작고 정확한 수정에는 MCP 파일 도구를 사용한다.
3. 안전한 설정 파일이 지속 운영 기억이 되어야 한다면 이 저장소에 미러링한다.
4. 사용자가 즉시 커밋을 요청하지 않는 한 Git 커밋은 주간 검토 지점으로 사용한다.
5. 더 큰 HA 설정 동기화에는 HA 쪽에서 validation 후 reload 또는 restart를 실행하는 pull script를 고려한다.

현재 MCP 경로는 실시간 Home Assistant 객체 관리와 통제된 YAML 수정에는 충분하다. 하지만 Git 이력, 백업, 넓은 설정 변경에 대한 신중한 검토를 대체해서는 안 된다.

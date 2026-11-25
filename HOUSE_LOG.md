# 집 운영 로그

- 2026-11-25 정리: 복구용 최신 사용량 카드 4개를 `Home Assistant/config/ui-lovelace.yaml` 백업에 반영하고 중복 `recovery/` 파일을 삭제했다. 향후 복원은 Git 이력을 사용한다.

## 2026-11-25

- HA 서버의 `ui-lovelace.yaml`을 다시 조회하여 11월 24일 수정한 사용량 ApexCharts 카드 4개가 저장된 상태임을 확인했다. 시간/일/월 통계는 `change`, 정렬은 `middle`, 현재 값 헤더는 `raw`이며 헤더 전용 일별 집계를 제거했다.
- `recovery/apexcharts-energy-cards.yaml`에 서버에서 추출한 카드 4개의 복구용 목록을 보관했다. 전체 대시보드 파일이 아니므로 원래 파일의 대응 카드만 교체해야 한다. 기본 대시보드는 `ui-lovelace.yaml`, 별도 SweetHome은 `dashboards/sweethome.yaml`로 구분한다.
- `history:` 추가 후 이력 조회가 정상화된 사실을 기록한다. 첫 카드의 `cache: false`는 진단 설정으로 유지되어 있다. 브라우저 렌더링은 이번 보관 작업에서 검증하지 않았다.

이 파일은 중요한 결정, 설정 이력, 운영 맥락을 기록한다.

## 2026-06-29

- 비서는 Home Assistant만이 아니라 집 전체를 관리하는 역할을 목표로 한다.
- Home Assistant, MCP 서버, IoT 연동은 현재 집 미니 PC에서 실행된다.
- Codex는 다른 컴퓨터와 다른 모델에서도 사용할 수 있다.
- 지속 운영 기억은 하나의 Codex 앱 설치나 채팅 스레드가 아니라 이 저장소에 남겨야 한다.
- 다른 컴퓨터는 이 저장소를 열고 미니 PC에 안전하게 연결하는 단말로 동작해야 한다.
- 향후 Codex 세션이 운영 맥락을 복원할 수 있도록 기본 문서들을 만들었다.
- 저장소를 GitHub `https://github.com/CrazyFunky/home-assistant.git`에 연결했다.
- 첫 커밋 `064b904 Initialize home operations docs`를 `main` 브랜치에 push했다.
- GitHub 접근은 컴퓨터별 로컬 자격 증명을 사용해야 한다. Codex가 GitHub Personal Access Token을 저장하거나 전달받지 않게 한다.
- HTTPS Git 접근에는 GitHub 웹사이트 비밀번호가 아니라 Personal Access Token이 필요하다.
- 새 컴퓨터에서는 Codex와 Git을 설치하고, 이 저장소를 clone하고, 로컬 자격 증명과 MCP 접근을 설정한 뒤, Codex에게 `AGENTS.md`와 관련 집 운영 문서를 읽게 한다.
- 현재 이어가기 프롬프트: `AGENTS.md를 먼저 읽고, HOUSE.md, MCP.md, DEVICES.md, OPERATIONS.md, HOUSE_LOG.md를 읽은 다음 우리 집 운영 비서 역할을 이어가.`
- `SETUP_NEW_PC.md`는 macOS와 Windows를 전체 작업 환경으로, 스마트폰을 검토/긴급 조작/이어가기 프롬프트용 가벼운 접근 단말로 다루어야 한다.
- Node-RED가 값을 직접 받아 변환하는 것을 확인한 뒤 오래된 Home Assistant 자동화 엔티티 `automation.decode_base64_sensor_value_2` (`Decode Base64 Sensor Value`)를 제거했다. 자동화 설정 삭제 API는 리소스를 찾을 수 없다고 응답했으므로, 대신 오래된 엔티티 레지스트리 항목을 제거했다. 자동화 수는 25개에서 24개로 변경되었다.
- Git 작업 선호도가 변경되었다. 작은 변경마다 커밋하지 말고, 일상적인 변경은 모아 두었다가 사용자가 즉시 커밋을 명시적으로 요청하지 않는 한 주 1회 요약 커밋으로 반영한다.
- 오래된 `Home Assistant 장비.xlsx` 인벤토리를 현재 HA 기준 workbook `outputs/ha_device_inventory_2026-06-29/Home Assistant 장비_HA기준_2026-06-29.xlsx`로 업데이트했다. 원본 A:J 열 구조를 유지하고, 민감한 `Local Key` 값은 비웠으며, 현재 Home Assistant 장치 레지스트리를 기준으로 사용했다.
- `SweetHome` storage 대시보드(`lovelace-sweetkitchen`)에 BTC, ETH, ONDO, TRUMP의 Binance USDT 가격 표시를 추가했다. `input_number` 헬퍼와 읽기 전용 markdown 카드를 사용했고, 각 심볼의 Binance 24시간 변동률도 함께 표시한다. 이것은 대시보드 표시 계층일 뿐이며, 자동 시장 데이터 갱신에는 `cryptoinfo_advanced`, REST YAML 센서, Node-RED 플로우 같은 지속 가능한 updater가 필요하다.
- 이 기기에서 Windows Codex 설정이 완료되었다. Git for Windows를 설치했고, `https://github.com/CrazyFunky/home-assistant.git`에서 저장소를 clone했으며, `main`은 `origin/main`을 추적한다.
- `SETUP_NEW_PC.md`에 깨져 있던 한국어 이어가기 프롬프트를 향후 Windows/macOS/스마트폰 세션에서 읽을 수 있는 한국어로 교체했다.
- 이 Windows 기기에서 Home Assistant MCP 연결을 확인했다. 로컬 프로젝트 MCP 설정은 ignored `.codex/config.toml`에 저장되고, 로컬 환경 힌트는 ignored `.env`에 저장된다.
- 이 Windows 프로젝트에 로컬/원격 Home Assistant 접근 프로필을 설정했다. 현재 PC는 기본적으로 로컬 LAN 프로필을 사용한다. 원격 HTTPS HA/MCP URL은 ignored 로컬 설정 파일에만 저장하며, MCP 비밀 경로는 추적 문서에 넣지 않는다.

## 2026-06-30

- Windows Codex 설정 후 macOS 저장소를 GitHub `main` 브랜치와 조정했다. 병합은 Mac의 대시보드/장치 인벤토리 커밋과 Windows의 로컬/원격 접근 프로필 문서를 모두 보존한다.
- 현재 음성 제어 구조: 선택된 Home Assistant 장치는 Matterbridge를 통해 Google Home에 노출되고, 가족 구성원은 Google 스피커의 음성 명령으로 제어한다. Home Assistant가 기준 시스템이며 Matterbridge와 Google Home은 음성 제어 브리지다.
- Home Assistant 접근 모델을 확인했다. 집 안 네트워크에서는 사설 IP 주소로, 집 밖에서는 외부 DNS 이름으로 Home Assistant에 접근할 수 있다. 정확한 주소는 로컬 전용으로 유지하고 커밋하지 않는다.
- 홈 네트워크 구조를 확인했다. 공인 인터넷은 유/무선 라우터로 들어오고, Home Assistant 서버, NAS 서버, 기타 유/무선 장치는 그 라우터 뒤에 있다. Home Assistant 서버에는 Zigbee 안테나가 연결되어 있고 Zigbee2MQTT를 실행하며, Nginx Proxy Manager도 실행하여 외부 DNS 접근을 설정된 내부 서비스로 라우팅한다.
- 현재 Codex 원격 MCP 경로를 확인했다. Codex는 외부 DNS 이름과 Nginx Proxy Manager 리버스 프록시를 통해 Home Assistant MCP 서버에 접근한다. 이 경로는 MCP/Home Assistant 접근 전용이며 Samba, SSH, NAS, 라우터 관리자, 임의의 LAN 서비스로 일반화하지 않는다.
- GitOps 가능성 점검을 완료했다. 현재 MCP 경로는 storage 대시보드, 자동화, 스크립트, add-on 인벤토리, HACS 메타데이터, 통합 메타데이터 같은 HA 설정 객체를 읽을 수 있지만, HA `/config` 파일시스템을 직접 나열하거나 읽을 수는 없었다. 향후 HA 설정 동기화를 위한 안전 후보 파일과 디렉터리를 `GITOPS.md`에 기록했다.
- MCP를 통해 Home Assistant 백업 가능성을 확인했다. 현재 14개의 snapshot 백업이 보이고 복원 기능도 있지만, 백업 복원은 범위가 넓고 영향을 크게 주므로 `ui-lovelace.yaml` 같은 파일 업데이트의 일반 경로가 아니라 복구/안전망으로 취급해야 한다.

## 2026-07-01

- SweetHome Binance 표시 경로를 `input_number.binance_*` 대시보드 직접 참조에서 BTCUSDT, ETHUSDT, ONDOUSDT, TRUMPUSDT 가격과 24시간 변동률을 표시하는 `sensor.binance_*` template sensor 헬퍼로 전환했다. 기존 updater 경로는 여전히 원래 input 헬퍼에 값을 공급하지만, 새 sensor 헬퍼가 값을 sensor 엔티티와 `state_class: measurement`로 노출하여 이 시점부터 Home Assistant가 sensor로 추적할 수 있게 했다.
- 후속 필요: 기존 Binance input 헬퍼는 검증 중 최근 recorder history를 보여주지 않았으므로, 장기적으로 더 나은 설계는 input-helper updater를 네이티브 Binance REST 센서 또는 다른 지속 가능한 sensor-producing 통합으로 교체하는 것이다. REST 센서는 YAML 설정과 Home Assistant 재시작이 필요하다.
- Binance 센서 마이그레이션을 완료했다. 안전한 파일/YAML 서비스를 사용할 수 있게 HA MCP Tools를 Home Assistant 통합으로 등록했고, `include/rest.yaml`에 BTCUSDT, ETHUSDT, ONDOUSDT, TRUMPUSDT의 Binance 24시간 ticker 데이터를 60초마다 polling하는 `rest:` 센서 블록을 추가했다. 임시 template sensor 헬퍼와 오래된 `input_number.binance_*` 헬퍼를 제거했다. `sensor.binance_*` 엔티티는 이제 Binance에서 직접 업데이트되고 `state_class: measurement`를 유지한다. recorder history는 다음 recorder/statistics 주기 후 다시 확인해야 한다.
- recorder 설정은 `homeassistant.packages: !include_dir_named include`를 통해 `include/recorder.yaml`에서 로드된다. recorder include 목록이 새 Binance 센서와 원래 맞지 않았으므로 `recorder.include.entity_globs`에 `sensor.binance_*`를 추가했다. Codex가 보호된 파일 경로를 통해 package 파일을 확인하고 수정할 수 있도록 HA MCP Tools extra allowed paths에 `include`를 추가했다.
- Binance REST 센서 블록을 `configuration.yaml`에서 `include/rest.yaml`로 옮긴 뒤 Home Assistant를 재시작하고 정상 검증했다. 8개의 `sensor.binance_*` 엔티티가 모두 live 값으로 돌아왔고, Binance 관련 시스템 로그 항목은 발견되지 않았으며, `sensor.binance_btcusdt_price`의 recorder history가 row를 반환하기 시작했다.
- Binance REST 센서가 대체한 뒤 오래된 `cryptoinfo_advanced` Bitcoin 센서를 `include/sensors.yaml`에서 제거했다. `include/recorder.yaml`에서도 `sensor.cryptoinfo_bitcoin_*` recorder include glob을 제거했다. 오래된 YAML sensor 엔티티가 state machine에서 사라지려면 Home Assistant 재시작이 필요하다.
- 오래된 crypto YAML 센서를 제거한 뒤 Home Assistant를 재시작했다. 이후 오래된 `sensor.cryptoinfo_bitcoin_price`와 `sensor.cryptoinfo_bitcoin_price_us` 레지스트리 항목을 제거했고, `ui-lovelace.yaml`을 업데이트하여 기존 두 줄짜리 Bitcoin 카드가 BTCUSDT, ETHUSDT, ONDOUSDT, TRUMPUSDT 네 개의 Binance 가격 센서를 표시하게 했다.
- 기본 YAML Lovelace 대시보드를 다시 업데이트하여 Binance 카드가 네 개 심볼 모두에 대해 가격과 24시간 변동률을 표시하게 했다. 카드는 이제 `sensor.binance_btcusdt_price`, `sensor.binance_btcusdt_24h_change`, `sensor.binance_ethusdt_price`, `sensor.binance_ethusdt_24h_change`, `sensor.binance_ondousdt_price`, `sensor.binance_ondousdt_24h_change`, `sensor.binance_trumpusdt_price`, `sensor.binance_trumpusdt_24h_change` 여덟 엔티티를 참조한다.
- 기본 YAML Lovelace Binance 카드를 여덟 개의 별도 entity row에서 심볼별 한 줄 markdown table로 압축했다. 각 row는 심볼, 현재 USDT 가격, 24시간 변동률을 보여준다.
- HACS를 통해 `lovelace-multiple-entity-row`를 설치하고 YAML-mode Lovelace resource로 `configuration.yaml`에 등록했다. 기본 YAML Lovelace Binance 카드는 이제 네 개의 `custom:multiple-entity-row` row를 사용하여 각 심볼의 현재 가격과 24시간 변동률을 한 줄에 표시한다.
- 기본 YAML Lovelace 대시보드의 Binance row를 조정하여 각 row에서 24시간 변동률이 현재 가격보다 앞에 보이게 했다.

## 2026-07-02

- Google Drive spreadsheet `Home Assistant 장비`를 현재 Home Assistant 장치 레지스트리 기준으로, 기존 `Home Network` sheet 구조를 유지한 채 제자리에서 업데이트했다. 여러 Zigbee 표시명을 수정했고, 오래된 `거실 Plug-Rear` row를 현재 등록된 `거실 프로젝터-Plug`로 교체했으며, 안방과 주방의 누락 Zigbee 장치를 추가하고, 현재 거실로 매핑되는 Bluetooth 온습도 row를 수정했다.
- Google Drive `Home Assistant 장비` spreadsheet의 `WIFI 기기` 구간을 라우터의 현재 장치 목록을 네트워크 기준으로 사용해 업데이트했다. sheet 구조를 유지하고 ID/Local Key 필드는 건드리지 않았으며, Home Assistant, Google 스피커, Smart Meter, cooktop, 거실 멀티탭, IAQ 센서, 프린터, 에어컨, 오븐, 관련 Wi-Fi 장치의 확인된 IP, MAC, 장비명 값을 맞췄다.

## 2026-08-26

- 거실 ESPHome 공기질 측정 장치의 현재 조립 형태를 확인했다. 부품은 ESP8266 NodeMCU v2, MH-Z19 CO2 센서, SDS011 미세먼지 센서, DHT11 온습도 센서로 구성되어 있다. SDS011을 기준 부품으로 두는 낮은 데스크탑형 환기 케이스 초안을 `designs/air_quality_case/`에 추가했다.
- Converted the SweetHome Binance display path from direct `input_number.binance_*` dashboard references to `sensor.binance_*` template sensor helpers for BTCUSDT, ETHUSDT, ONDOUSDT, and TRUMPUSDT prices and 24-hour changes. The existing updater path still feeds the original input helpers, while the new sensor helpers expose the values as sensor entities with `state_class: measurement` so Home Assistant can begin tracking them as sensors from this point forward.
- Follow-up needed: the existing Binance input helpers did not show recent recorder history during verification, so the stronger long-term design is to replace the input-helper updater with native Binance REST sensors or another durable sensor-producing integration. REST sensors require YAML configuration and a Home Assistant restart.
- Completed the Binance sensor migration. HA MCP Tools was registered as a Home Assistant integration so safe file/YAML services became available, then `include/rest.yaml` received a `rest:` sensor block that polls Binance 24-hour ticker data for BTCUSDT, ETHUSDT, ONDOUSDT, and TRUMPUSDT every 60 seconds. The temporary template sensor helpers and the older `input_number.binance_*` helpers were removed. `sensor.binance_*` entities now update directly from Binance and keep `state_class: measurement`; recorder history should be rechecked after the next recorder/statistics cycle.
- Recorder configuration is loaded from `include/recorder.yaml` via `homeassistant.packages: !include_dir_named include`. The recorder include list did not originally match the new Binance sensors, so `sensor.binance_*` was added to `recorder.include.entity_globs`. HA MCP Tools extra allowed paths now include `include` so Codex can inspect and update these package files through the guarded file path.
- After moving the Binance REST sensor block out of `configuration.yaml` and into `include/rest.yaml`, Home Assistant was restarted and validated successfully. All eight `sensor.binance_*` entities came back with live values, no Binance-related system log entries were found, and recorder history began returning rows for `sensor.binance_btcusdt_price`.
- The older `cryptoinfo_advanced` Bitcoin sensors were removed from `include/sensors.yaml` after the Binance REST sensors replaced them. The `sensor.cryptoinfo_bitcoin_*` recorder include glob was also removed from `include/recorder.yaml`; a Home Assistant restart is needed for the old YAML sensor entities to disappear from the state machine.
- Home Assistant was restarted after removing the old crypto YAML sensors. The stale `sensor.cryptoinfo_bitcoin_price` and `sensor.cryptoinfo_bitcoin_price_us` registry entries were then removed, and `ui-lovelace.yaml` was updated so the former two-row Bitcoin card now shows four Binance price sensors: BTCUSDT, ETHUSDT, ONDOUSDT, and TRUMPUSDT.
- The default YAML Lovelace dashboard was updated again so the Binance card shows both price and 24-hour percentage change for all four tracked symbols. The card now references eight entities: `sensor.binance_btcusdt_price`, `sensor.binance_btcusdt_24h_change`, `sensor.binance_ethusdt_price`, `sensor.binance_ethusdt_24h_change`, `sensor.binance_ondousdt_price`, `sensor.binance_ondousdt_24h_change`, `sensor.binance_trumpusdt_price`, and `sensor.binance_trumpusdt_24h_change`.
- The default YAML Lovelace Binance card was compacted from eight separate entity rows into one markdown table with one row per symbol. Each row shows symbol, current USDT price, and 24-hour percentage change.
- `lovelace-multiple-entity-row` was installed through HACS and registered as a YAML-mode Lovelace resource in `configuration.yaml`. The default YAML Lovelace Binance card now uses four `custom:multiple-entity-row` rows so each symbol shows current price and 24-hour percentage change on one row.
- The Binance rows in the default YAML Lovelace dashboard were adjusted so the 24-hour percentage change appears before the current price on each row.

## 2026-07-03

- Dashboard file organization policy clarified: keep Home Assistant's default root-level files such as `configuration.yaml`, `automations.yaml`, `scripts.yaml`, `scenes.yaml`, `secrets.yaml`, and `ui-lovelace.yaml` under `/config`, while placing user-created supporting files in purpose-specific folders such as `dashboards/`, `include/`, `www/`, and `themes/`.
- The shared `button_card_templates.yaml` file was moved from `/config/button_card_templates.yaml` to `/config/dashboards/button_card_templates.yaml`. The root `ui-lovelace.yaml` now references it with `button_card_templates: !include dashboards/button_card_templates.yaml`; future YAML dashboard files inside `/config/dashboards/` can reference the same file with `button_card_templates: !include button_card_templates.yaml`.
- Voice-control operating policy clarified: Matterbridge is the default path for exposing Home Assistant devices to Google Home, while the Home Assistant `google_assistant` integration is kept only as an exception path for entities that need Google-specific handling. The live `google_assistant.yaml` file was converted into the package file `/config/include/google_assistant.yaml`; `configuration.yaml` no longer includes it directly, and Home Assistant config validation passed after the change. The Google service account JSON was moved to `/config/secrets/google_assistant_service_account.json`; it remains secret material and must not be committed.
- Presence detection policy clarified: family presence should be based on Wi-Fi router tracking rather than requiring every family member to install the Home Assistant Companion app. The `person.weinhwan` helper was simplified to use only `device_tracker.iptime_inhwan_we`; the spouse and children person helpers already use their corresponding `device_tracker.iptime_*` entities. Automations should continue to reference `person.*` entities rather than raw device trackers.
- The extra `person.detion` entity was removed from family presence tracking and kept only as a Home Assistant user identity. The active person entities are now the four household members whose presence is backed by ipTIME Wi-Fi trackers.
- The live `/config/include/device_tracker.yaml` file was cleaned up with comments documenting the family presence mapping and phone replacement rule: keep target names stable and update only the MAC address when a phone changes. Home Assistant config validation passed after the cleanup.
- Created `HOME_ASSISTANT_INSTALL_GUIDE.md` as the baseline guide for choosing and preparing a Home Assistant host. The preferred production path is a low-power mini server running Home Assistant OS; Synology Container and Raspberry Pi HA OS are documented as alternate paths with tradeoffs.
- Binance dashboard change percentages were redesigned from Binance's rolling 24-hour `priceChangePercent` to a daily 09:00 KST baseline. Four `input_number.binance_*_0900_price` helpers store the daily base price, automation `automation.binance_09_00_baseline_prices` refreshes them every day at 09:00, `/config/include/rest.yaml` now keeps only the live price REST sensors, and `/config/include/templates.yaml` reuses the existing `sensor.binance_*_24h_change` unique IDs as 09:00-baseline percentage template sensors. `/config/ui-lovelace.yaml` headers were changed from `24h` to `09:00`; Home Assistant config validation passed, but a restart is required for the REST/template entity swap to take effect.
- A safe Git backup folder, `Home Assistant/`, was created from the live `/config` tree. It includes root YAML files, `include/`, `dashboards/`, and Lovelace assets under `www/lovelace/`, while excluding `secrets.yaml`, `/config/secrets/`, `.storage/`, databases, logs, generated backups, tokens, certificates, keys, and temporary `*.bak_codex_*` files. A stale commented Telegram API key value was sanitized in both the Git backup and the live `configuration.yaml`; Home Assistant config validation passed afterward.

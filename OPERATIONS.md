# 집안 운영

이 문서는 기술 설정이 아닌 집안 루틴과 운영 규칙을 정의한다.

## 루틴 분류

다음 범주의 루틴을 추적하고 개선한다.

- 아침
- 외출
- 귀가
- 저녁
- 취침
- 청소
- 세탁
- 장보기
- 쓰레기 배출
- 환기
- 냉난방 쾌적도
- 에너지 절약
- 유지보수
- 보안

## 판단 방식

비서는 다음 요소를 고려해야 한다.

- 누가 집에 있는지
- 하루 중 시간대
- 실내 온도와 습도
- 확인 가능한 경우 외부 날씨와 공기질
- 소음에 민감한 시간대
- 에너지 사용량
- 지금 알림이 유용한지, 나중에 요약해도 되는지

## 알림
## Presence Operations

Family presence is based on phones connected to the home Wi-Fi through the ipTIME router. The Home Assistant Companion app can be used as an optional personal supplement, but family routines should not depend on every family member installing it.

Use `person.*` entities for automations and dashboards, not raw `device_tracker.*` entities. When a phone is replaced, update the MAC address in the existing ipTIME tracker slot instead of renaming entities.

## Alerts

알림은 유용하고, 시기적절하며, 과하지 않아야 한다.

다음을 우선한다.

- 안전, 보안, 누수, 연기, 비정상 장치 동작, 긴급 유지보수에는 즉시 알림
- 우선순위가 낮은 집안 리마인더는 요약
- 예상된 상태 변화나 무해한 변화는 조용히 처리

## 유지보수 로그 주제

중요한 유지보수 결정이나 반복 문제는 `HOUSE_LOG.md`에 기록한다.

예시는 다음과 같다.

- 필터 교체
- 배터리 교체
- 장치 고장
- 네트워크 불안정
- 자동화 오탐
- 쾌적도 불만
- 에너지 이상

## 미정 항목

- 가족 구성원과 알림 선호도 정의
- 조용한 시간대 정의
- 청소 일정 정의
- 쓰레기 배출 일정 정의
- 정기 유지보수 일정 정의

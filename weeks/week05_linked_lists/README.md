# Week 5 - Linked Lists

- 교재 범위: 7.Linked Lists
- 이번 주 LeetCode 태그: **Linked List**


## 개념 한 줄 요약

(이론 30% 대비 — 이번 챕터 핵심 개념을 배운 직후 여기에 3줄 이내로 정리)

-
-
-

## 풀이 로그

| 날짜 | 문제 (LeetCode #) | 태그 | 난이도 | 소요시간 | 접근 방식 요약 | 시간/공간복잡도 | 막힌 점 / 복습 필요 |
|---|---|---|---|---|---|---|---|
| 10-05 | 206 Reverse Linked List | Linked List | Easy | 35min | prev/current 두 포인터로 순회하며 다음 노드를 미리 저장한 뒤 현재 노드의 next를 prev로 돌려 제자리에서 리스트를 뒤집음 | 시간 O(n), 공간 O(1) | `current.next`를 바꾸기 전에 `next_node`에 먼저 저장해야 뒤 노드를 잃지 않음을 기억하기 |

풀이 코드는 `solutions/문제번호_영문슬러그.py` 형식으로 저장하세요.

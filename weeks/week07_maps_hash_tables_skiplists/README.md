# Week 7 - Maps, Hash Tables, Skip Lists

- 교재 범위: 10.Maps, Hash Tables, and Skip Lists
- 이번 주 LeetCode 태그: **Hash Table, Hash Map, Design**


## 개념 한 줄 요약

(이론 30% 대비 — 이번 챕터 핵심 개념을 배운 직후 여기에 3줄 이내로 정리)

-
-
-

## 풀이 로그

| 날짜 | 문제 (LeetCode #) | 태그 | 난이도 | 소요시간 | 접근 방식 요약 | 시간/공간복잡도 | 막힌 점 / 복습 필요 |
|---|---|---|---|---|---|---|---|
| 10-13 | 1 Two Sum | Array, Hash Table | Easy | 15min | 해시맵에 값 → 인덱스를 저장하며 순회하다가, 현재 값의 보수(target - 현재 값)가 이미 맵에 있으면 그 인덱스와 현재 인덱스를 반환 | 시간 O(n), 공간 O(n) | 같은 원소를 두 번 쓰지 않도록 맵에 저장하기 전에 보수를 먼저 확인하는 순서 기억하기 |
| 10-13 | 167 Two Sum II - Input Array Is Sorted | Array, Two Pointers | Medium | 15min | 정렬된 배열의 양 끝에 포인터를 두고, 합이 target보다 크면 오른쪽 포인터를 줄이고 작으면 왼쪽 포인터를 늘려 합이 같아지는 쌍을 찾음 | 시간 O(n), 공간 O(1) | 배열이 정렬되어 있을 때만 가능한 방식이며, 반환하는 인덱스는 1부터 시작하므로 각각 +1 해야 함을 기억하기 |

풀이 코드는 `solutions/문제번호_영문슬러그.py` 형식으로 저장하세요.

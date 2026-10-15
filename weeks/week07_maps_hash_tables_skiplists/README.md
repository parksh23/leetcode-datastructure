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
| 10-14 | 380 Insert Delete GetRandom O(1) | Array, Hash Table, Design | Medium | 35min | 값을 리스트에 저장하고 해시맵에 값 → 인덱스를 함께 유지하며, 삭제 시 삭제할 값 자리에 마지막 원소를 옮긴 뒤 pop해서 O(1)로 삭제하고 getRandom은 리스트에서 무작위로 선택 | 시간 O(1) (평균, 모든 연산), 공간 O(n) | 마지막 원소를 옮길 때 해시맵의 그 원소 인덱스도 함께 갱신해야 하고, 삭제할 값이 마지막 원소인 경우를 따로 처리해야 함을 기억하기 |
| 10-14 | 387 First Unique Character in a String | Hash Table, String | Easy | 35min | 해시맵으로 문자별 등장 횟수를 먼저 센 뒤, 문자열을 앞에서부터 다시 순회하며 처음으로 횟수가 1인 문자의 인덱스를 반환 | 시간 O(n), 공간 O(1) (알파벳 26자로 제한) | 딕셔너리를 순회하지 않고 원래 문자열 순서로 다시 확인해야 "첫 번째" 위치를 보장할 수 있음을 기억하기 |
| 10-15 | 205 Isomorphic Strings | Hash Table, String | Easy | 15min | s→t, t→s 두 방향의 해시맵을 만들어 같은 인덱스의 문자 쌍이 기존 매핑과 충돌하면 False를 반환하고, 끝까지 충돌이 없으면 True | 시간 O(n), 공간 O(1) (문자 집합 크기에 한정) | 한 방향 매핑만 확인하면 서로 다른 문자가 같은 문자로 매핑되는 경우(예: "ab"→"aa")를 놓치므로 양방향 매핑이 필요함을 기억하기 |
| 10-15 | 242 Valid Anagram | Hash Table, String, Sorting | Easy | 15min | 두 문자열의 길이가 다르면 바로 False, 같으면 각각 문자별 등장 횟수를 딕셔너리로 세어 두 딕셔너리가 같은지 비교 | 시간 O(n), 공간 O(1) (문자 종류 수에 한정) | 길이를 먼저 비교해 빠르게 걸러낼 수 있고, collections.Counter나 정렬 후 비교(O(n log n))로도 풀 수 있음을 기억하기 |
| 10-15 | 290 Word Pattern | Hash Table, String | Easy | 25min | s를 공백으로 split해 패턴 길이와 단어 수를 먼저 비교하고, 패턴 문자↔단어 양방향 해시맵으로 기존 매핑과 충돌하면 False | 시간 O(n), 공간 O(n) | 패턴 길이와 단어 수가 다른 경우를 먼저 걸러야 하고, 205와 같은 양방향 매핑(일대일 대응) 아이디어임을 기억하기 |

풀이 코드는 `solutions/문제번호_영문슬러그.py` 형식으로 저장하세요.

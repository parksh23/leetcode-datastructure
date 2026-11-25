# Week 10~11 - Search Trees

- 교재 범위: 11.Search Trees
- 이번 주 LeetCode 태그: **Binary Search Tree, Binary Search**
- 일정: **11/16 3차 퀴즈**

## 개념 한 줄 요약

(이론 30% 대비 — 이번 챕터 핵심 개념을 배운 직후 여기에 3줄 이내로 정리)

-
-
-

## 풀이 로그

| 날짜 | 문제 (LeetCode #) | 태그 | 난이도 | 소요시간 | 접근 방식 요약 | 시간/공간복잡도 | 막힌 점 / 복습 필요 |
|---|---|---|---|---|---|---|---|
| 11-23 | 215 Kth Largest Element in an Array | Array, Heap (Priority Queue), Divide and Conquer | Medium | 30min | 크기 k짜리 최소 힙을 유지하며 배열을 순회. 힙에 k개가 찰 때까지 push하고, 이후에는 현재 값이 힙의 최솟값(min_heap[0])보다 클 때만 heappushpop으로 교체해, 끝에 힙의 루트(min_heap[0])가 k번째로 큰 값이 되도록 함 | 시간 O(n log k), 공간 O(k) | 최대 힙이 아니라 크기 k의 최소 힙을 쓰는 이유(루트가 k번째 큰 값)를 기억하기. 정렬(O(n log n))이나 퀵셀렉트(평균 O(n))로도 풀 수 있음 |
| 11-25 | 347 Top K Frequent Elements | Array, Hash Table, Heap (Priority Queue), Bucket Sort | Medium | 40min | Counter로 원소별 등장 횟수를 센 뒤, (빈도, 값) 튜플을 크기 k짜리 최소 힙에 유지. 힙에 k개가 찰 때까지 push하고 이후에는 현재 빈도가 힙의 최소 빈도(min_heap[0][0])보다 클 때만 heappushpop으로 교체해, 끝에 힙에 남은 값들을 반환 | 시간 O(n log k), 공간 O(n) (Counter) + O(k) (힙) | 215와 같은 "크기 k 최소 힙" 패턴이고, 힙의 기준이 값이 아니라 빈도라 (빈도, 값) 순서로 넣어야 함을 기억하기. 버킷 정렬(빈도별 리스트)을 쓰면 O(n)에도 가능 |

풀이 코드는 `solutions/문제번호_영문슬러그.py` 형식으로 저장하세요.

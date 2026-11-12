# Week 12~14 - Graph Algorithms

- 교재 범위: 14.Graph Algorithms
- 이번 주 LeetCode 태그: **Graph, BFS/DFS, Union Find, Topological Sort, Shortest Path**
- 일정: **11/30 4차 퀴즈**

## 개념 한 줄 요약

(이론 30% 대비 — 이번 챕터 핵심 개념을 배운 직후 여기에 3줄 이내로 정리)

-
-
-

## 풀이 로그

| 날짜 | 문제 (LeetCode #) | 태그 | 난이도 | 소요시간 | 접근 방식 요약 | 시간/공간복잡도 | 막힌 점 / 복습 필요 |
|---|---|---|---|---|---|---|---|
| 11-11 | 841 Keys and Rooms | Graph, BFS, DFS | Medium | 30min | 0번 방에서 시작해 큐(deque)로 BFS를 수행하며, 방에서 얻은 열쇠(인접 방)가 아직 방문하지 않은 방이면 큐에 넣고 visited 집합에 추가한 뒤, 끝에 방문한 방의 수가 전체 방 수와 같은지로 판단 | 시간 O(V + E), 공간 O(V) | 큐에 넣는 시점에 visited에 추가해 같은 방이 중복으로 들어가지 않게 하는 점 기억하기. 로컬 실행 시 `from collections import deque` import 필요 |
| 11-12 | 323 Number of Connected Components in an Undirected Graph | Graph, DFS, Union Find | Medium | 40min | 간선 리스트로 양방향 인접 리스트를 만들고, 0~n-1 노드를 순회하며 아직 방문하지 않은 노드를 만날 때마다 컴포넌트 수를 1 늘리고 DFS로 연결된 노드를 모두 방문 처리 | 시간 O(V + E), 공간 O(V + E) | 무방향 그래프라 간선을 양쪽(u→v, v→u)에 모두 추가해야 하고, 간선이 없는 고립 노드도 컴포넌트로 세기 위해 0~n-1을 전부 순회해야 함을 기억하기. Union Find로도 풀 수 있음. 로컬 실행 시 `List` import 필요 |

풀이 코드는 `solutions/문제번호_영문슬러그.py` 형식으로 저장하세요.

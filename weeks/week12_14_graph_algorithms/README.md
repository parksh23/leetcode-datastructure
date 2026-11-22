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
| 11-15 | 207 Course Schedule | Graph, DFS, Topological Sort, Cycle Detection | Medium | 40min | 선수 과목 관계를 방향 그래프 인접 리스트로 만들고, 상태 배열(0=미방문, 1=방문 중, 2=완료)을 둔 DFS로 사이클을 탐지. 방문 중(1)인 노드를 다시 만나면 사이클이므로 False, 모든 노드를 탐색하고도 사이클이 없으면 True | 시간 O(V + E), 공간 O(V + E) | 단순 visited 집합이 아니라 "현재 DFS 경로상(1)"과 "탐색 완료(2)"를 구분해야 사이클을 정확히 잡을 수 있고, 그래프가 여러 컴포넌트일 수 있어 모든 노드에서 DFS를 시작해야 함을 기억하기. 위상 정렬(Kahn 알고리즘, 진입차수)로도 풀 수 있음 |
| 11-16 | 785 Is Graph Bipartite? | Graph, DFS, BFS, Union Find | Medium | 40min | 노드 색을 colors 배열(0=미방문, 1/-1=두 색)로 관리하며 DFS로 탐색. 인접 노드가 현재 노드와 같은 색이면 이분 그래프가 아니므로 False, 미방문이면 반대 색(-color)을 칠하고 재귀 탐색. 연결되지 않은 컴포넌트가 있을 수 있어 모든 노드에서 시작 | 시간 O(V + E), 공간 O(V) | 그래프가 여러 컴포넌트로 나뉠 수 있으므로 미방문 노드마다 DFS를 시작해야 하고, 인접 노드와 같은 색이 나오는 순간 바로 False를 반환해야 함을 기억하기. BFS나 Union Find로도 풀 수 있음 |
| 11-18 | 1135 Connecting Cities With Minimum Cost | Graph, Union Find, Minimum Spanning Tree | Medium | 65min | 크루스칼 알고리즘으로 간선을 비용 오름차순으로 정렬한 뒤, Union-Find(경로 압축)로 서로 다른 집합의 도시만 연결하며 비용을 누적. 선택한 간선이 n-1개가 되면 최소 비용을 반환하고, 끝까지 n-1개를 못 채우면 연결이 불가능하므로 -1 반환 | 시간 O(E log E) (정렬), 공간 O(n) | 도시 번호가 1부터 시작하므로 parents를 n+1 크기로 만들어야 하고, 간선이 n-1개 미만이면 바로 -1을 반환할 수 있음을 기억하기. 경로 압축과 union by rank를 함께 쓰면 더 빠름. 로컬 실행 시 `List` import 필요 |
| 11-22 | 743 Network Delay Time | Graph, Heap, Shortest Path, Dijkstra | Medium | 50min | 간선 리스트로 인접 리스트(defaultdict)를 만들고, 최소 힙에 (누적 거리, 노드)를 넣는 다익스트라로 시작 노드 k에서 각 노드까지의 최단 거리를 dist에 확정. 힙에서 꺼낸 노드가 처음 방문이면 거리를 확정하고 이웃을 push하며, 끝에 모든 노드에 도달했으면 최대 거리, 아니면 -1 반환 | 시간 O(E log V), 공간 O(V + E) | 같은 노드가 힙에 여러 번 들어갈 수 있으므로 꺼낼 때 이미 확정된 노드는 건너뛰어야 하고, 도달 불가능한 노드가 있는지는 len(dist) == n으로 확인해야 함을 기억하기. 음수 간선이 없을 때만 다익스트라 사용 가능 |
| 11-22 | 200 Number of Islands | Array, Matrix, BFS, DFS, Union Find | Medium | 60min | 격자를 순회하다 땅("1")을 만나면 섬 개수를 1 늘리고 BFS로 상하좌우로 연결된 땅을 모두 "0"으로 바꿔 방문 처리하여 같은 섬이 중복으로 세어지지 않게 함 | 시간 O(R × C), 공간 O(min(R, C)) (BFS 큐, 최악 O(R × C)) | 큐에 넣는 시점에 바로 "0"으로 바꿔야 같은 칸이 중복으로 큐에 들어가지 않고, 경계 검사(0 <= nr < row)를 먼저 해야 함을 기억하기. 입력 grid를 직접 수정하므로 원본 보존이 필요하면 visited 사용. 로컬 실행 시 `List` import 필요 |
| 11-22 | 1584 Min Cost to Connect All Points | Array, Graph, Heap, Minimum Spanning Tree | Medium | 35min | 프림 알고리즘으로 0번 점에서 시작해 최소 힙에서 가장 싼 간선의 도착점을 방문 처리하며 비용을 누적. 점이 방문될 때마다 아직 방문하지 않은 모든 점까지의 맨해튼 거리를 힙에 push하고, 모든 점이 방문되면 총 비용을 반환 | 시간 O(n² log n), 공간 O(n²) (완전 그래프이므로 간선이 O(n²)) | 힙에서 꺼낸 노드가 이미 방문된 경우 건너뛰어야 하고, 점이 많은 완전 그래프에서는 크루스칼보다 프림이 간선을 따로 만들지 않아 간단함을 기억하기. 1135와 같은 MST 문제 |

풀이 코드는 `solutions/문제번호_영문슬러그.py` 형식으로 저장하세요.

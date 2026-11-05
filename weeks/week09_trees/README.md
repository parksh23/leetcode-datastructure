# Week 9 - Trees

- 교재 범위: 8.Trees
- 이번 주 LeetCode 태그: **Tree, Binary Tree, DFS, BFS**


## 개념 한 줄 요약

(이론 30% 대비 — 이번 챕터 핵심 개념을 배운 직후 여기에 3줄 이내로 정리)

-
-
-

## 풀이 로그

| 날짜 | 문제 (LeetCode #) | 태그 | 난이도 | 소요시간 | 접근 방식 요약 | 시간/공간복잡도 | 막힌 점 / 복습 필요 |
|---|---|---|---|---|---|---|---|
| 11-05 | 113 Path Sum II | Tree, Binary Tree, DFS, Backtracking | Medium | 45min | DFS로 루트부터 내려가며 현재 경로(path)와 누적합을 유지하다가, 리프 노드에서 누적합이 targetSum과 같으면 경로를 복사(list(path))해 정답에 추가하고, 탐색이 끝난 노드는 path.pop()으로 되돌려(백트래킹) 다른 가지에 영향이 없게 함 | 시간 O(n²) (최악: 경로 복사 비용 포함), 공간 O(h) (재귀 깊이와 path, 정답 제외) | 정답에 path를 그대로 넣지 않고 list(path)로 복사해야 하고, 리프가 아닌 노드에서도 pop이 실행되도록 반환 전에 항상 path.pop()을 호출하는 구조 기억하기 |
| 11-05 | 543 Diameter of Binary Tree | Tree, Binary Tree, DFS | Easy | 45min | 후위 순회 DFS로 각 노드의 왼쪽/오른쪽 깊이를 구해, 그 합(left + right)으로 해당 노드를 지나는 최장 경로를 계산하고 전체 최댓값(self.result)을 갱신하며, 부모에게는 max(left, right) + 1 깊이를 반환 | 시간 O(n), 공간 O(h) (재귀 깊이) | 지름은 루트를 지나지 않을 수도 있으므로 모든 노드에서 left + right를 갱신해야 하고, 반환값(깊이)과 갱신값(지름)이 다르다는 점 기억하기 |

풀이 코드는 `solutions/문제번호_영문슬러그.py` 형식으로 저장하세요.

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
| 11-07 | 104 Maximum Depth of Binary Tree | Tree, Binary Tree, DFS | Easy | 35min | 재귀 DFS로 빈 노드는 깊이 0을 반환하고, 그 외에는 왼쪽·오른쪽 서브트리 깊이 중 큰 값에 1을 더해 반환 | 시간 O(n), 공간 O(h) (재귀 깊이, 최악 O(n)) | 기저 조건(빈 노드 = 0)과 자신의 깊이를 더하는 +1 위치를 기억하기. BFS로 레벨 수를 세는 방법도 가능 |
| 11-07 | 117 Populating Next Right Pointers in Each Node II | Tree, Linked List, BFS | Medium | 70min | 이미 연결된 next 포인터를 이용해 레벨 단위로 순회하며, 더미 노드와 tail 포인터로 다음 레벨의 노드들을 왼쪽→오른쪽 순서로 이어 붙이고 다음 레벨의 첫 노드(dummy.next)로 이동 | 시간 O(n), 공간 O(1) (큐 없이 next 포인터 활용) | 완전 이진 트리가 아니라서 자식이 한쪽만 있거나 없는 경우를 각각 확인해야 하고, 레벨마다 dummy를 새로 만들어야 이전 레벨과 섞이지 않음을 기억하기. 로컬 실행 시 Node 클래스 정의 필요 |
| 11-07 | 236 Lowest Common Ancestor of a Binary Tree | Tree, Binary Tree, DFS | Medium | 70min | 재귀 DFS로 root가 None이거나 p 또는 q이면 root를 반환하고, 왼쪽·오른쪽 서브트리 결과가 둘 다 있으면 현재 root가 LCA, 한쪽만 있으면 그 결과를 위로 전달 | 시간 O(n), 공간 O(h) (재귀 깊이) | p와 q가 서로의 조상인 경우 먼저 발견한 노드를 그대로 반환해도 올바른 이유(나머지 하나는 그 서브트리 안에 존재)를 이해해 두기 |
| 11-08 | 105 Construct Binary Tree from Preorder and Inorder Traversal | Array, Hash Table, Tree, Divide and Conquer | Medium | 80min | 전위 순회의 현재 원소가 루트임을 이용해, 중위 순회에서 루트 위치를 해시맵으로 O(1)에 찾아 구간을 왼쪽/오른쪽 서브트리로 나누고 재귀로 트리를 구성. preorder_index를 하나씩 증가시키며 루트를 소비 | 시간 O(n), 공간 O(n) (해시맵 + 재귀 깊이) | 왼쪽 서브트리를 먼저 만들어야 preorder_index 순서가 맞으므로 left → right 호출 순서가 중요하고, 중위 구간(left, right)의 종료 조건(left > right)을 기억하기. 로컬 실행 시 TreeNode 정의 필요 |
| 11-08 | 606 Construct String from Binary Tree | String, Tree, DFS | Easy | 50min | 전위 순회 재귀로 루트 값을 문자열로 만들고, 자식이 하나라도 있으면 왼쪽 결과를 괄호로 감싸 붙이며(왼쪽이 없어도 빈 괄호 "()" 유지), 오른쪽 자식이 있을 때만 오른쪽 결과를 괄호로 감싸 붙임 | 시간 O(n), 공간 O(h) (재귀 깊이, 문자열 연결 비용 제외) | 왼쪽 자식이 없고 오른쪽만 있을 때는 "()"를 반드시 남겨야 하고, 오른쪽이 없으면 불필요한 괄호를 생략하는 조건 구분 기억하기 |

풀이 코드는 `solutions/문제번호_영문슬러그.py` 형식으로 저장하세요.

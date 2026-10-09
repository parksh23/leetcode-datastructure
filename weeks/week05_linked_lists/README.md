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
| 10-06 | 141 Linked List Cycle | Linked List, Two Pointers | Easy | 45min | 빠른 포인터는 두 칸, 느린 포인터는 한 칸씩 이동하는 Floyd 토끼와 거북이 방식으로 두 포인터가 만나면 사이클이 있다고 판단 | 시간 O(n), 공간 O(1) | 빠른 포인터가 두 칸 이동할 때마다 `None`인지 확인해야 `next` 접근 에러를 피할 수 있음을 기억하기 |
| 10-07 | 876 Middle of the Linked List | Linked List, Two Pointers | Easy | 20min | 빠른 포인터는 두 칸, 느린 포인터는 한 칸씩 이동시켜 빠른 포인터가 끝에 도달했을 때 느린 포인터가 가리키는 노드를 중간 노드로 반환 | 시간 O(n), 공간 O(1) | 노드 개수가 짝수일 때는 두 번째 중간 노드를 반환해야 하므로 빠른 포인터가 `None`이 되는 시점의 종료 조건 확인하기 |
| 10-07 | 86 Partition List | Linked List, Two Pointers | Medium | 35min | x보다 작은 노드와 크거나 같은 노드를 각각 더미 헤드를 가진 두 리스트로 나눠 이어 붙이고, 뒤쪽 리스트의 끝을 None으로 끊은 뒤 두 리스트를 연결 | 시간 O(n), 공간 O(1) | 큰 값 리스트의 마지막 노드의 next를 `None`으로 끊지 않으면 사이클이 생길 수 있음을 기억하기 |
| 10-09 | 21 Merge Two Sorted Lists | Linked List | Easy | 15min | 더미 헤드를 두고 두 리스트의 현재 노드 값을 비교해 더 작은 노드를 결과 리스트 뒤에 이어 붙이며 전진하고, 한쪽이 끝나면 남은 리스트를 통째로 연결 | 시간 O(n + m), 공간 O(1) | 반복문이 끝난 뒤 남은 리스트를 이어 붙이는 것을 잊지 말고, 반환은 더미 헤드의 `next`임을 기억하기 |
| 10-09 | 143 Reorder List | Linked List, Two Pointers | Medium | 40min | 빠른/느린 포인터로 중간을 찾아 리스트를 둘로 끊고, 뒤쪽 절반을 뒤집은 뒤 앞쪽 절반과 한 노드씩 번갈아 끼워 넣어 제자리에서 재배치 | 시간 O(n), 공간 O(1) | 중간에서 `slow.next = None`으로 끊지 않으면 사이클이 생기며, 번갈아 연결할 때 다음 노드를 먼저 저장해야 함을 기억하기 |

풀이 코드는 `solutions/문제번호_영문슬러그.py` 형식으로 저장하세요.

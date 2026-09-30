# Week 4 - Stacks, Queues, Deques

- 교재 범위: 6.Stacks, Queues, and Deques
- 이번 주 LeetCode 태그: **Stack, Queue, Monotonic Stack, Design**
- 일정: **9/23 1차 퀴즈**

## 개념 한 줄 요약

(이론 30% 대비 — 이번 챕터 핵심 개념을 배운 직후 여기에 3줄 이내로 정리)

-
-
-

## 풀이 로그

| 날짜 | 문제 (LeetCode #) | 태그 | 난이도 | 소요시간 | 접근 방식 요약 | 시간/공간복잡도 | 막힌 점 / 복습 필요 |
|---|---|---|---|---|---|---|---|
| 09-26 | 20 Valid Parentheses | Stack | Easy | 35min | 여는 괄호는 스택에 push하고, 닫는 괄호는 스택에서 pop한 값과 짝이 맞는지 확인하며 끝까지 순회 후 스택이 비었는지로 판단 | 시간 O(n), 공간 O(n) | 스택이 비어있을 때 pop하면 에러가 나므로 길이 체크를 먼저 하는 순서 기억하기 |
| 09-28 | 1047 Remove All Adjacent Duplicates In String | Stack, String | Easy | 30min | 문자를 스택에 쌓다가 바로 위 문자와 같으면 pop, 다르면 push해서 인접한 중복 쌍을 계속 제거 | 시간 O(n), 공간 O(n) | 스택이 비어있는 상태에서 바로 위 문자와 비교하지 않도록 `if stack and ...` 조건 순서 기억하기 |
| 09-29 | 155 Min Stack | Stack, Design | Medium | 45min | 값을 push할 때마다 보조 스택(min_stack)에 지금까지의 최솟값도 함께 push해서 getMin을 O(1)에 조회 | 시간 O(1) (모든 연산), 공간 O(n) | pop할 때 원래 스택과 min_stack을 항상 같이 pop해서 두 스택의 길이를 맞춰야 함을 기억하기 |
| 09-30 | 622 Design Circular Queue | Queue, Design, Array | Medium | 35min | 고정 크기 배열과 start/end 포인터를 나머지 연산으로 순환시켜 큐를 구현하고, current_len으로 가득 참/비어있음을 판단 | 시간 O(1) (모든 연산), 공간 O(k) | Rear는 다음에 넣을 위치(end)의 바로 앞 원소를 가리켜야 하므로 `end - 1` 인덱스를 참조해야 함을 기억하기 |

풀이 코드는 `solutions/문제번호_영문슬러그.py` 형식으로 저장하세요.

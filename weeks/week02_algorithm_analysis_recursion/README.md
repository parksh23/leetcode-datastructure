# Week 2 - Algorithm Analysis / Recursion

- 교재 범위: 3.Algorithm Analysis, 4.Recursion
- 이번 주 LeetCode 태그: **Recursion, Math, Divide and Conquer**

## 개념 한 줄 요약

(이론 30% 대비 — 이번 챕터 핵심 개념을 배운 직후 여기에 3줄 이내로 정리)

- 

- 

- 

## 풀이 로그


| 날짜    | 문제 (LeetCode #) | 태그        | 난이도  | 소요시간  | 접근 방식 요약         | 시간/공간복잡도                                     | 막힌 점 / 복습 필요                      |
| ----- | --------------- | --------- | ---- | ----- | ---------------- | -------------------------------------------- | --------------------------------- |
| 09-07 | 509, 70         | recursion | Easy | 25min | fibonacci 기반의 접근 | 509: 시간 O(2^n), 공간 O(n) 70: 시간 O(n), 공간 O(1) | Fibonacci 방식을 시간 문제 해결을 위해 DP로 접근 |
| 09-08 | 136 Single Number | Hash Table | Easy | 15min| 집합에 처음 나온 수를 추가하고, 다시 나온 수는 제거하여 하나만 남은 수를 반환 | 시간 O(n), 공간 O(n) | XOR를 사용하면 공간복잡도를 O(1)로 줄일 수 있으므로 복습 필요 |
| 09-08 | 22 Generate Parentheses | Recursion, Backtracking | Medium | 30min | 여는 괄호는 n개 미만일 때, 닫는 괄호는 여는 괄호보다 적을 때만 추가하며 재귀 탐색 | 시간 O(n·Cₙ), 공간 O(n·Cₙ), 보조 공간 O(n) | 유효한 접두사만 탐색하도록 하는 두 조건을 기억하기 |
| 09-09 | 50 Pow(x, n) | Math, Recursion, Divide and Conquer | Medium | 40min| 음수 지수는 역수로 바꾸고, 지수를 절반씩 나누는 빠른 거듭제곱으로 재귀 계산 | 시간 O(log \|n\|), 공간 O(log \|n\|) | Python 3에서는 재귀 호출의 `n/2`를 정수 나눗셈 `n//2`로 바꿔야 함 |


풀이 코드는 `solutions/문제번호_영문슬러그.py` 형식으로 저장하세요.

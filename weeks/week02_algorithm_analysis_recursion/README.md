# Week 2 - Algorithm Analysis / Recursion

- 교재 범위: 3.Algorithm Analysis, 4.Recursion
- 이번 주 LeetCode 태그: **Recursion, Math, Divide and Conquer**

## 개념 한 줄 요약

(이론 30% 대비 — 이번 챕터 핵심 개념을 배운 직후 여기에 3줄 이내로 정리)

- 시간복잡도는 반복·재귀 호출 횟수로, 공간복잡도는 추가 자료구조와 재귀 호출 스택까지 포함해 입력 크기에 따라 분석한다.
- 재귀는 종료 조건과 입력이 줄어드는 과정을 먼저 확인하고, 같은 부분 문제가 반복되면 메모이제이션으로 중복 계산을 줄인다.
- 분할 정복은 문제를 나누어 결과를 합친다. 지수를 절반씩 줄이는 거듭제곱은 O(log n)이지만, 모든 분할을 탐색하면 경우의 수가 크게 늘 수 있다.

## 풀이 로그


| 날짜    | 문제 (LeetCode #) | 태그        | 난이도  | 소요시간  | 접근 방식 요약         | 시간/공간복잡도                                     | 막힌 점 / 복습 필요                      |
| ----- | --------------- | --------- | ---- | ----- | ---------------- | -------------------------------------------- | --------------------------------- |
| 09-07 | 509, 70         | recursion | Easy | 25min | fibonacci 기반의 접근 | 509: 시간 O(2^n), 공간 O(n) 70: 시간 O(n), 공간 O(1) | Fibonacci 방식을 시간 문제 해결을 위해 DP로 접근 |
| 09-08 | 136 Single Number | Hash Table | Easy | 15min| 집합에 처음 나온 수를 추가하고, 다시 나온 수는 제거하여 하나만 남은 수를 반환 | 시간 O(n), 공간 O(n) | XOR를 사용하면 공간복잡도를 O(1)로 줄일 수 있으므로 복습 필요 |
| 09-08 | 22 Generate Parentheses | Recursion, Backtracking | Medium | 30min | 여는 괄호는 n개 미만일 때, 닫는 괄호는 여는 괄호보다 적을 때만 추가하며 재귀 탐색 | 시간 O(n·Cₙ), 공간 O(n·Cₙ), 보조 공간 O(n) | 유효한 접두사만 탐색하도록 하는 두 조건을 기억하기 |
| 09-09 | 50 Pow(x, n) | Math, Recursion, Divide and Conquer | Medium | 40min| 음수 지수는 역수로 바꾸고, 지수를 절반씩 나누는 빠른 거듭제곱으로 재귀 계산 | 시간 O(log \|n\|), 공간 O(log \|n\|) | Python 3에서는 재귀 호출의 `n/2`를 정수 나눗셈 `n//2`로 바꿔야 함 |
| 09-11 | 231 Power of Two | Math, Bit Manipulation | Easy | 15min | 2의 거듭제곱은 이진수에서 1비트가 하나뿐이라는 성질을 이용해 `n & (n - 1)`이 0인지 확인 | 시간 O(1), 공간 O(1) | `n & (n - 1)`이 최하위 1비트를 제거하는 원리와 `n > 0` 조건 기억하기 |
| 09-12 | 268 Missing Number | Array, Math, Bit Manipulation | Easy | 20min | `1…n`과 배열의 모든 원소를 XOR하여 두 번 등장하는 값들을 소거하고 누락된 수를 계산 | 시간 O(n), 공간 O(1) | XOR의 교환·결합 법칙과 같은 수를 두 번 XOR하면 0이 되는 성질 기억하기 |
| 09-12 | 241 Different Ways to Add Parentheses | Recursion, Divide and Conquer | Medium | 40min | 각 연산자를 분할점으로 삼아 왼쪽·오른쪽 부분식의 결과를 재귀적으로 구한 뒤 모든 조합을 계산 | 시간 O(Cₘ), 공간 O(Cₘ + m) (m은 연산자 수) | 같은 부분식을 반복 계산하므로 메모이제이션을 적용하는 방법 복습하기 |
| 09-14 | 204 Count Primes | Array, Math, Number Theory | Medium | 35min | 에라토스테네스의 체를 사용해 각 소수의 제곱부터 n 미만의 배수를 합성수로 표시 | 시간 O(n log log n), 공간 O(n) | 배수 제거를 `i²`부터 시작하는 이유와 사용하지 않는 내부 함수 매개변수 정리하기 |
| 09-16 | 486 Predict the Winner | Recursion, Dynamic Programming, Game Theory | Medium | 50min | 양끝 숫자 중 하나를 고른 뒤 상대와의 최대 점수 차를 재귀적으로 계산하여 최종 점수 차가 0 이상인지 확인 | 시간 O(2ⁿ), 공간 O(n) | 같은 `(left, right)` 구간을 반복 계산하므로 메모이제이션을 적용해 시간 O(n²)로 개선하기 |


풀이 코드는 `solutions/문제번호_영문슬러그.py` 형식으로 저장하세요.

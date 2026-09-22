# Week 3 - Array-Based Sequences

- 교재 범위: 5.Array-Based Sequences
- 이번 주 LeetCode 태그: **Array, String, Two Pointers, Sliding Window**


## 개념 한 줄 요약

(이론 30% 대비 — 이번 챕터 핵심 개념을 배운 직후 여기에 3줄 이내로 정리)

-
-
-

## 풀이 로그

| 날짜 | 문제 (LeetCode #) | 태그 | 난이도 | 소요시간 | 접근 방식 요약 | 시간/공간복잡도 | 막힌 점 / 복습 필요 |
|---|---|---|---|---|---|---|---|
| 09-14 | 283 Move Zeroes | Array, Two Pointers | Easy | 20min | 앞에서부터 0이 아닌 값을 다음 위치에 덮어쓰고, 남은 뒷부분을 0으로 채움 | 시간 O(n), 공간 O(n) | 현재 슬라이스 대입은 임시 0 리스트를 생성하므로 반복문으로 채워 보조 공간 O(1) 달성하기 |
| 09-15 | 125 Valid Palindrome | String, Two Pointers | Easy | 15min | 소문자로 변환한 뒤 양끝 포인터에서 영숫자가 아닌 문자를 건너뛰며 같은지 비교 | 시간 O(n), 공간 O(n) | 전체 문자열의 소문자 복사 대신 비교할 문자만 변환하면 보조 공간을 줄일 수 있음 |
| 09-15 | 643 Maximum Average Subarray I | Array, Sliding Window | Easy | 15min | 처음 k개 합을 구한 뒤 창이 이동할 때 빠진 값은 빼고 새 값은 더해 최대 합을 갱신 | 시간 O(n), 공간 O(k) | `nums[:k]` 슬라이스가 임시 리스트를 생성하므로 직접 합산하면 보조 공간 O(1) 가능 |
| 09-19 | 724 Find Pivot Index | Array, Prefix Sum | Easy | 15min | 전체 합에서 왼쪽 누적합과 현재 값을 빼 오른쪽 합을 구하고, 양쪽 합이 같아지는 첫 인덱스를 반환 | 시간 O(n), 공간 O(1) | 현재 값을 왼쪽 합에 더하기 전에 비교해야 하며, 양 끝 인덱스도 확인하기 |
| 09-21 | 1480 Running Sum of 1d Array | Array, Prefix Sum | Easy | 20min | 두 번째 원소부터 직전 누적합을 현재 값에 더해 입력 배열 자체를 누적합 배열로 변경 | 시간 O(n), 공간 O(1) | 입력 배열을 직접 변경하는 제자리 풀이임을 기억하고, 원본 보존이 필요한 경우 구분하기 |
| 09-21 | 209 Minimum Size Subarray Sum | Array, Sliding Window | Medium | 35min | 오른쪽 포인터로 합을 늘리고 목표 이상이면 왼쪽 포인터를 옮기며 최소 길이를 갱신 | 시간 O(n), 공간 O(1) | 원소가 모두 양수라서 합이 커지고 작아지는 방향이 보장될 때만 이 방식이 가능함 |
| 09-21 | 560 Subarray Sum Equals K | Array, Hash Table, Prefix Sum | Medium | 50min | 현재 누적합에서 k를 뺀 누적합의 등장 횟수를 해시맵에서 찾아 정답에 더함 | 시간 O(n), 공간 O(n) | 누적합 0의 빈도를 처음부터 1로 두면 시작 인덱스가 0인 경우를 별도 조건 없이 처리 가능 |
| 09-21 | 728 Self Dividing Numbers | Math | Easy | 30min | 각 자리 숫자로 나누어떨어지는지 divmod로 하나씩 확인하고, 자리 숫자에 0이 있거나 나누어떨어지지 않으면 제외 | 시간 O((right-left)·d), 공간 O(1) (결과 리스트 제외) | divmod로 자리수를 분리하는 방법과 0으로 나눌 때 예외 처리하는 조건 기억하기 |
| 09-22 | 338 Counting Bits | Dynamic Programming, Bit Manipulation | Easy | 30min | 이전 계산값을 재사용해 `i>>1`의 비트 수에 `i`의 최하위 비트를 더하는 점화식으로 각 수의 1의 개수를 구함 | 시간 O(n), 공간 O(1) (결과 리스트 제외) | 최하위 비트를 제거한 값의 결과를 재사용하는 점화식을 세우는 방법 복습하기 |
| 09-22 | 3 Longest Substring Without Repeating Characters | Hash Table, String, Sliding Window | Medium | 60min | 해시맵으로 각 문자의 등장 여부를 추적하며 오른쪽 포인터를 넓히고, 중복이 나오면 왼쪽 포인터를 좁혀 최대 길이를 갱신 | 시간 O(n), 공간 O(min(n, 문자 종류 수)) | 문자 등장 횟수를 0/1로만 관리하는 로직이 왼쪽 포인터를 한 칸씩만 옮겨도 항상 맞는지 검증하기 |

풀이 코드는 `solutions/문제번호_영문슬러그.py` 형식으로 저장하세요.

# 자료구조 LeetCode 매일 풀이 로그

이번 학기 자료구조 과목(부산대, 2026 가을) 코딩 시험 대비를 위한 매일 LeetCode 풀이 · 인증 레포입니다.

## 사용 방법

1. 오늘이 몇 주차인지 [SCHEDULE.md](./SCHEDULE.md)에서 확인하고, 그 주차 폴더(`weeks/weekNN_.../`)로 이동합니다.
2. 해당 주차 태그로 LeetCode에서 문제를 골라 풉니다 (Easy → Medium 순).
3. 푼 코드는 그 주차 폴더의 `solutions/`에 `문제번호_영문슬러그.py` 형식으로 저장합니다.
4. 그 주차 폴더의 `README.md` 로그 표에 한 줄 기록을 추가합니다.
5. 커밋 & 푸시 = 그날의 인증입니다.

```
git add weeks/weekNN.../solutions/xxx.py weeks/weekNN.../README.md
git commit -m "day: LC 123 문제이름 (태그) - week NN"
git push
```

## 진행 체크

전체 진행 체크리스트는 [PROGRESS.md](./PROGRESS.md)를 참고하세요.

## 폴더 구조

```
weeks/
  week02_algorithm_analysis_recursion/
  week03_array_based_sequences/
  week04_stacks_queues_deques/
  week05_linked_lists/
  week06_trees/
  week07_priority_queues/
  week08_midterm_review/
  week09_maps_hash_tables_skiplists/
  week10_11_search_trees/
  week12_14_graph_algorithms/
  week15_final_review/
```

각 폴더에는 그 주차의 학습 로그 템플릿(`README.md`)과 풀이 코드를 담는 `solutions/`가 있습니다.

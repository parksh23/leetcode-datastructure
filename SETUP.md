# 새 GitHub 레포로 올리는 방법

1. GitHub에서 새 레포를 만듭니다 (예: `leetcode-datastructure`). README 없이 빈 상태로 생성하세요.
2. 아래 명령을 이 폴더에서 실행합니다 (URL은 본인 레포 주소로 교체):

```bash
git remote add origin https://github.com/<username>/leetcode-datastructure.git
git branch -M main
git push -u origin main
```

3. 이후로는 평소처럼 `git add`, `git commit`, `git push`만 반복하면 됩니다.

> 자동 추천 스케줄을 쓰려면 이 레포를 **Public**으로 만드는 걸 추천합니다. Private으로 유지하려면 매번 접근 인증이 별도로 필요합니다.

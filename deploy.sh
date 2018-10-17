#!/usr/bin/env bash
# git add -A
git add -A

# requirements만들기
pipenv lock --requirements > requirements.txt

# .secrets의 requirements를 staging area에 추가
git add -f .secrets/ requirements.txt

# eb deloy실행
eb deploy --profile jsm-eb-user --staged

# .secerets와 requirements를 staging area에서 제거
git reset HEAD .secrets/ requirements.txt

git reset HEAD

# requirements.txt삭제
rm requirements.txt

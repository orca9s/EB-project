#!/usr/bin/env bash
# git add -A
git add -A

# requirements만들기
pipenv lock --requirements > requirements.txt

# .secrets의 requirements를 staging area에 추가
git add -f .secrets/ requirements.txt
git status
echo "git add 안되는 파일 강제로 추가"

# eb deloy실행
eb deploy --profile jsm-eb-user --staged
echo "staged 영역에서 배포시작"

# .secerets와 requirements를 staging area에서 제거
git reset HEAD .secrets/ requirements.txt
echo "staged 영역에 강제로 추가한 파일들 다시 해제"

git reset HEAD
echo "staged 영역에 추가한 파일 전부 해제"

# requirements.txt삭제
rm requirements.txt
echo "requirements 제거"
git status
echo "배포완료"

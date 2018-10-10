#!/usr/bin/env python
import os
import subprocess

try:
    # pipenv lock으로 requiremets.txt생성
    subprocess.call('pipenv lock --requirements > requirements.txt', shell=True)

    # docker build
    subprocess.call('docker build -t eb-docker:base -f Dockerfile.base .', shell=True)
finally:
    # 끝난 후 requirements.txt파일 삭제
    os.remove('requirements.txt')
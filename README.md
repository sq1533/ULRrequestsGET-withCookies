# alarmErrorCodeCheck
Pandas, requests, re

## 구성
* errorCode.py

## 목적
알람 미정의 에러코드 수집을 위한 자동분류 시스템

## 기대효과
* 알람 에러코드 확인을 위한 ULR진입 및 수기 진행 자동화
* 기존 3시간 작업 수행시간 10분 내외 단축

## 기능
* .csv파일 내 URL 수집 및 session정보 cookies에 첨부 및 requests.get 요청
* HTML내 text 데이터 수집 및 정제, 미정의 오류코드 확인 및 저장

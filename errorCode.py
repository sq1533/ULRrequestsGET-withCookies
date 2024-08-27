import json
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
#세션 정보 호출
with open("C:\\Users\\USER\\ve_1\\DB\\9session.json", "r", encoding="utf-8") as f:
    session = json.load(f)
def missingError(service:str):
    #알람 데이터 정제
    alarmData = pd.read_csv(f"C:\\Users\\USER\\Downloads\\NAVER WORKS\\{service}.csv",sep="\n\n",header=None,engine='python')
    urlList = alarmData[alarmData[0].str.contains("●실시간 상황 URL링크: ",case=False)].index.tolist()
    #오류코드 확인
    for i in urlList:
        url = alarmData.loc[i][0].replace("●실시간 상황 URL링크: ","")
        cookies = {
            'YourSession':session['YourSession'],
            'JSESSIONID':session['JSESSIONID']
        }
        html = requests.get(url, cookies=cookies).text
        if '오류코드:' in html:
            soup = BeautifulSoup(html.split('오류코드:')[1],'html.parser')
            #숫자 및 텍스트 혼합 패턴 정의
            pattern = re.compile(r"<b>([\w\s]+)</b>(\(([^\)]+)\)|([\w\s]+))?")
            matches = pattern.findall(str(soup))
            for match in matches:
                if match[0] in match[1]:
                    print(url)
                    print(match[0])
                else:
                    pass
        else:
            pass
    print("-"*50)
missingError("간편결제")
missingError("VAN")
missingError("PG")
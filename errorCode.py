import json
import os
import re
import requests
import pandas as pd
#세션 정보 호출
sessionPath = os.path.join(os.path.dirname(__file__),"session.json")
with open(sessionPath, "r", encoding="utf-8") as f:
    session = json.load(f)
def missingError(service:str):
    #알람 데이터 정제
    alarmData = pd.read_csv(f"C:\\Users\\USER\\Downloads\\NAVER WORKS\\{service}.csv",sep="\n\n",header=None,engine='python')
    urlList = alarmData[alarmData[0].str.contains("●실시간 상황 URL링크: ",case=False)].index.tolist()
    newline = []
    #오류코드 확인
    for i in urlList:
        url = alarmData.loc[i][0].replace("●실시간 상황 URL링크:","").replace(" ","")
        cookies = {
            'YourSession':session['YourSession'],
            'JSESSIONID':session['JSESSIONID']
        }
        html = requests.get(url, cookies=cookies).text
        if '오류코드:' in html:
            text = html.split('오류코드:')[1].split('</div>')[0]
            cleanText = re.sub(r"<[^>]+>","",text) #HTML 태그 제거
            #오류코드 및 괄호 안 오류코드 추출
            pattern = r"(\w+)\(([^)]+)\)"
            matches = re.findall(pattern,cleanText)
            results = [list(item) for item in matches]
            for j in range(len(results)):
                if results[j][0]==results[j][1]:
                    newline.append(url)
                    newline.append(results[j][0])
                else:pass
            pd.Series(newline).to_csv(f"C:\\Users\\USER\\ve_1\\alarmErrorCode\\{service}.csv",index=False,sep="\n")
        else:pass
missingError("간편결제")
missingError("VAN")
missingError("PG")
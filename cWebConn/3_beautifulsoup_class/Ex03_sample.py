"""
    기상청 사이트에서 필요한 데이타를 추출하고자 한다면?
        - 데이타 가져오기     ` requests 모듈
                             ` urllib.request 모듈의 urlopen() 이용
        - 데이타 추출    BeautifulSoup 이용
"""

from bs4 import BeautifulSoup
from urllib import request as req


# 1. 데이타 가져오기
rssUrl = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
res = req.urlopen(rssUrl)


# 2. 필요 데이타 추출하기

soup = BeautifulSoup(res,'html.parser')
#print(soup)

# 도시(city) / 시간대별 날씨(wf)
city = soup.find_all('city')
data = soup.find_all('data')
tmEf = soup.select('body data tmef')
tmEf = soup.find_all('location tmef')
wf = soup.find_all('wf')
print(tmEf)
print(wf)
for c in city:
    print(c.text,"지역의 날씨")




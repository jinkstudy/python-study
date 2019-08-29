"""
    기상청 사이트에서 필요한 데이타를 추출하고자 한다면?
        - 데이타 가져오기     ` requests 모듈
                             ` urllib.request 모듈의 urlopen() 이용
        - 데이타 추출    BeautifulSoup 이용
"""

from bs4 import BeautifulSoup
from urllib import request as req


# 1. 데이타 가져오기

res = req.urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
returnData = res.read().decode('utf-8')
#print(returnData)

# 2. 필요 데이타 추출하기

soup = BeautifulSoup(returnData,'html.parser')
green = soup.select('.green')
#print(green)

for g in green :
    print(g.text)

"""
http://www.seoul.go.kr > 청사안내 > 자치구
https://www.seoul.go.kr/seoul/autonomy.do

BeautifulSoup  : 파서를 이용해서 html 의 요소를 추출하게 해주는 모듈
        - 단점은 개행문자를 고려해야 한다
Tag : 태그
NavigableString : 원래는 tag 사이의 문자열

#  xpath를 사용하면 개행문자를 고려하지 않아도 된단다
#  https://developer.mozilla.org/ko/docs/XPath
"""

import requests
from bs4 import BeautifulSoup, NavigableString

# 웹 문서 가져오기
url = 'https://www.seoul.go.kr/seoul/autonomy.do'


# 구청이름 / 구청주소 / 구청전화번호  / 구청 홈페이지

res = requests.get(url)
#print(res.text)

soup = BeautifulSoup(res.text,'html.parser')
district_list = soup.select('.tabcont')
#print(district_list)

index = ['구청주소','구청 전화번호','구청홈페이지']
for district in district_list:
    print()
    print("구청이름:",district.select_one('strong').text)
    print("--" * 20)
    #print(district.select_one('ul').text)

    info = district.select('li')

    for i,l in enumerate(info):
        print(index[i],":",l.text)
    print("**" * 20)

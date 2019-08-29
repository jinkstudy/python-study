'''
 [과제] 교보문고에서 파이썬 책 검색하여
    - csv 파일로 저장
    - mysql 테이블에 저장
'''


from urllib.request import urlopen
from bs4 import BeautifulSoup

# 교보문고 > '파이썬' 검색 > 국내도서
html = urlopen("http://www.kyobobook.co.kr/search/SearchKorbookMain.jsp?vPstrCategory=KOR&vPstrKeyWord=python&vPplace=top")

# BeaurifulSoup을 이용해서 총 책의 권수를 출력하기
# 책의 제목들을 출력

soup = BeautifulSoup(html,'html.parser')


title = soup.select('.title strong')
count = len(title)
print("*"*50)
print("총", count,"권의 책이 조회 되었습니다.")
print("*"*50)
for i,t in enumerate(title):
    print(i+1,">>",t.text)




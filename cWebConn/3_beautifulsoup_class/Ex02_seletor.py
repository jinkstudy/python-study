"""
    BeautifulSoup 모듈에서
    - HTML의 구조(=트리구조)에서 요소를 검색할 때 : find() / find_all()
    - 속성을 검색할 때 :  attrs()
    - CSS 선택자 검색할 때 : select() /  select_one()
"""

from bs4 import BeautifulSoup

html = """
    <html><body>
        <div id='course'>
            <h1>빅데이터 과정</h1>
        </div>
        <div id='subjects'> 
            <ul class='subs'>
                <li>머신러닝</li>
                <li>데이터 처리</li>
                <li>데이타 분석</li>
            </ul>
        </div>
    </body></html>
"""
soup = BeautifulSoup( html ,'html.parser')

#2. id 값으로 검색
h1 = soup.select_one('#course > h1')
print(h1) #<h1>빅데이터 과정</h1>
print(h1.string) #빅데이터 과정

print("*"*50)
# 3. class값으로 검색 - 목록(li) 내용 출력

h1 = soup.select('.subs > li')
for h in h1:
    print(h.text)

print("*" * 50)


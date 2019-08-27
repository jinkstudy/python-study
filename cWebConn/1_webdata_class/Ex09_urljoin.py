"""
 urllib.parse.urljoin() : 상대경로를 절대경로로 변화하는 함수
"""


from urllib import parse
baseUrl = 'http://www.example.com/html'
print(parse.urljoin(baseUrl,'b.html')) #http://www.example.com/b.html
print(parse.urljoin(baseUrl,'/c.html')) #http://www.example.com/c.html
print(parse.urljoin(baseUrl,'../sub/d.html')) #http://www.example.com/sub/d.html
print(parse.urljoin(baseUrl,'sub/e.html')) #http://www.example.com/sub/e.html
print(parse.urljoin(baseUrl,'/sub/f.html')) #http://www.example.com/sub/f.html

#완전한 형태를 갖춘 url인 경우 덮어쓰기 됨.
print(parse.urljoin(baseUrl,'http://www.mysite.com/mypage.jsp'))
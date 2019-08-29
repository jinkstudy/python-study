'''
1. 크롬웹드라이버로 구글 사이트 열기

2. 실제 크롬창에서 '플레이데이터'라고 검색버튼을 누른다.
    개발자모드(F12)에서 이 부분을 보면
    <input name='q' value='플레이데이터'~~ >
    그리고 'google검색' 버튼이 type='submit' 인거 확인
'''

# [1]
from selenium import webdriver

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')

# 2. 페이지 접근
driver.get('https://www.pji.co.kr/menu/menuList.jsp?cl_cd=1')

# [2]
bt = driver.find_elements_by_css_selector('.menu_img')
for a in bt:
    print(a.text)







#----------------------------------------------
# [2]


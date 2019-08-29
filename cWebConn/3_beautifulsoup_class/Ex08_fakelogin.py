"""
    일단 http://www.hanbit.co.kr 회원가입

    [예] 한빗출판네트워크 ( 단순 페이지 ) : 이 예문은 위키북스 출판사 교재 예문임
                                    <파이썬을 이용한 머신러닝, 딥러닝 실전개발 예문>
    로그인페이지 : http://www.hanbit.co.kr/member/login.html
    마이페이지 : http://www.hanbit.co.kr/myhanbit/membership.html

    1. 로그인 페이지에서 개발자모드에서 로그인 form 태그를 분석
        입력태그의 name='m_id' / name='m_passwd' 확인

    2. 로그인 후에 마이페이지에서 마일리지와 한빛이코인 부분
        마일리지 (.mileage_section1 > span ) / 한빛이코인 (.mileage_section2 > span )

    3. 로그인과정에 어떤 통신이 오가는지 분석
        Network > Preserve log 체크 > Doc 탭을 선택하고 다시 처음부터 로그인을 하면 서버와 통신을 오고간다
        이 때 Name 중 login_proc.php를 선택하고 Headers 부분을 확인한다
        
        Gereral : Request Mathod : POST
        Form Data : m_id와 m_passwd 값 확인
"""

import requests
from bs4 import BeautifulSoup

#세션 시작하기(쿠키, 권한 등을 요청하기 위해 사용하는 객체)

sess = requests.session() #session을 가져오는 함수
login_info = {
    'm_id' : '',
    'm_passwd' : ''
}

url_login = "http://www.hanbit.co.kr/member/login_proc.php"
res = sess.post(url_login,data=login_info) # url_login 페이지를 post방식으로 요청하겠다.
res.raise_for_status() #해당 사이트의 오류 발생 시 예외 발생.

url_mypage = 'http://www.hanbit.co.kr/myhanbit/myhanbit.html'
res = sess.get(url_mypage)
res.raise_for_status()

#결과값 파싱하여 원하는 데이터 얻어오기.
soup = BeautifulSoup(res.text,'html.parser')
#print(soup)

mile = soup.select_one('.mileage_section1 span')
print("마일리지는:", mile.text)
mile1 = soup.select_one('.mileage_section2 span')
print("한빛 이코인은:", mile1.text)




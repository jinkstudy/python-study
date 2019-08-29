"""
    [연습] 페이스북에 접속해서 로그인 하기

        로그인 후에 보안창은 없는데 안 넘어가서

        from selenium.webdriver.common.keys import Keys

        아이디와 패스워드 지정후에
        elem.send_keys(Keys.RETURN)

"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

myID = 'sweetyks486@gmail.com'
myPW = ''


# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver')
driver.implicitly_wait(3) # 암묵적으로 자원로드될 때까지 3초 기다림

# 네이버로그인 하기 -[결론] 네이버 보안에 걸림
# 보안에 안걸렸으면 로그인된 상태로 많은 정보를 가져올 수 있다
driver.get('https://www.facebook.org')
elem =driver.find_element_by_id('email')
elem.send_keys(myID)

elem = driver.find_element_by_id('pass')
elem.send_keys(myPW)
# 로그인 버튼을 눌러주자.
#driver.find_element_by_xpath('//*[@id="u_0_2"]/fieldset/input').click()
elem.send_keys(Keys.RETURN)
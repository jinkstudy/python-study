"""
    이메일 주소의 적합성 체크
        kim@encore.com   : 올바른 이메일
        kim@encore       : 잘못된 이메일 ( . 하나 없어서 )
        kim_@encore.com  : 잘못된 이메일 ( 특수문자 안됨 )

     [참고]
        ^[]: 시작
        [^] : not
        {2,9} : 최소 2개 최대 9개
        {2,} : 최소 2개만 지정하고 최대는 지정하지 않음
        $ 끝
"""
import re
def email_check(email):
    a = re.split('@',email)
    if(len(a)>1) :
        id = a[0]
        add = a[1]
        dot =re.split('\.',add)
        #print(dot)
        if len(re.findall('[\W]', id)) > 0:
            print("id에는 특수문자를 포함할 수 없습니다")
        elif len(dot) !=2 or '' in dot:
            print("이메일을 확인하세요 ex)aa.com, bb.net")
        else :
            print("올바른 이메일입니다.")
    else :
        print("@가 없습니다. 이메일을 확인하세요")
    return

email_check('kim@encore.com')       # 올바른 이메일
email_check('kim@.com')           # 잘못된 이메일 ( . 하나 없어서 )
email_check('k!m_@encore.com')      # 잘못된 이메일 ( 특수문자 안됨 )

import re
def email_check1(email):
    #exp = re.findall('^[\w]{5,10}@[a-z]+\.[a-z]+',email)
    exp = re.findall('^[\w]@[a-z]+\.[a-z]+$',email)
    if len(exp) == 0:
        print('잘못된 이메일')
    else : print('올바른 이메일')


email_check1('kim@encore.com')       # 올바른 이메일
email_check1('kim@.com')           # 잘못된 이메일 ( . 하나 없어서 )
email_check1('k!m_@encore.com')      # 잘못된 이메일 ( 특수문자 안됨 )

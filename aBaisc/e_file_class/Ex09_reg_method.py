"""
    # 패턴과 소스를 비교하는 메소드
    - match() : 패턴의 일치여부 확인
    - findall() : 일치하는 모든 문자열 리스트 반환
    - search() : 첫번째 일치하는 객체 반환
    - split() : 패턴에 맞게 소스를 분리한 후 문자열 조각의 리스트 반환
    - sub() : 대체 인자로 변환하는 함수
"""

import re

# match()
msg = 'We are happy. You are happy. Happy2019 2020'


result = re.match('.*happy',msg)  #We are happy. You are happy #happy까지 찾아줌
if result:
    print(result.group())

result1 = re.match('.*2019',msg)  #We are happy. You are happy. Happy2019 //2019까지 찾아줌.
if result1:
    print(result1.group())

result1 = re.match('happy',msg)  #아무것도 안나옴 //happy로 시작하는 것을 찾기 때문.
if result1:
    print(result1.group())

# search()
result = re.search('happy',msg)
if result:
    print(result.group()) #happy

# split()
result = re.split('a',msg) #a를 기점으로 자름
if result:
    print(result) #['We ', 're h', 'ppy. You ', 're h', 'ppy. H', 'ppy2019 2020']


# sub()
result = re.sub('a','@',msg) #a를 @로 바꿈 #We @re h@ppy. You @re h@ppy. H@ppy2019 2020
print(result)


import re

# findall(검색어, 문자열) : 문자열에서 검색어와 일하는 내용들을 리스트로 반환

msg = 'We_are_happy!! You are happy?? Happy2019-2020 안녕'

a = re.findall('happy',msg) #['happy', 'happy']
print(a)

a = re.findall('Happy',msg) #['Happy']
print(a)

## 소문자 모두 찾기
a = re.findall('[a-z]',msg) #['e', 'a', 'r', 'e', 'h', 'a', 'p', 'p', 'y', 'o', 'u', 'a', 'r', 'e', 'h', 'a', 'p', 'p', 'y', 'a', 'p', 'p', 'y']
print(a)

## 소문자 아닌 것 모두 찾기
a = re.findall('[^a-z]',msg)
print(a) #['W', '_', '_', '!', '!', ' ', 'Y', ' ', ' ', '?', '?', ' ', 'H', '2', '0', '1', '9', '-', '2', '0', '2', '0', ' ', '안', '녕']

## 소문자로만 이루어진것 찾기
a = re.findall('[a-z]+',msg)
print(a) #['e', 'are', 'happy', 'ou', 'are', 'happy', 'appy']


##소문자와 대문자로 이루어진 단어 찾기
a = re.findall('[a-zA-Z]+',msg)
print(a) #['We', 'are', 'happy', 'You', 'are', 'happy', 'Happy']

## 숫자 찾기
a = re.findall('[0-9]',msg)
print(a) #['2', '0', '1', '9', '2', '0', '2', '0']

#소문자,대문자,숫자가 아닌것
a = re.findall('[^0-9a-zA-Z]',msg)
print(a) #['_', '_', '!', '!', ' ', ' ', ' ', '?', '?', ' ', '-', ' ', '안', '녕']

#문자,_,숫자_를 검색
a = re.findall('[\w]+',msg) #['We_are_happy', 'You', 'are', 'happy', 'Happy2019', '2020', '안녕']
print(a)


#문자, 숫자_ 가 아닌 것을 검색
a = re.findall('[\W]',msg)
print(a) #['!', '!', ' ', ' ', ' ', '?', '?', ' ', '-', ' ']



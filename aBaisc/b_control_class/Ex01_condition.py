"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록을 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자

    [ex]
    if a>b:
        print(a)
            print(b)  => 에러발생

    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            문장들
        else :
            문장들

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass
        ` 파이썬은 switch 문 없음
"""

# 거짓(False)의 값
i = 0;
i2=0.0
i3=""
i4=str()
i5=list()
i6=tuple()
i7=set()
i8=dict()
i9={}
i10=None


# (1) 간단한 if 확인
a = -1
if a :
    print('True-1')  # True
else:
    print('False-1')

if not a:
    print('True-2') # 수행안됨.


#(2) 논리 연산자 이용한 조건
a = -1
b = 10
if a and b :
    print('True-3')
if a or b:
    print('True-4')

print(a and b) #b 출력 , 만약 0이 있다면 0출력
print (a or b) #a 출력 , 만약 0이 있다면 0이 아닌 다른 값 출력


#(3) find()- 해당글자를 찾으면 그 글자의 인덱스 반환
print('=='*50)
word = 'korea'
if word.find('k'):
    print('1>')

print('=='*50)
if word.find('z'):
    print('2>')
print('=='*50)

if word.find('k') in range(len(word)):
    print('3>')
print('=='*50)


#(3) 변수

a,b = 0,1
if a:
    c=2
elif b:
    c=4
else:
    c=8
print('C=',c) #C=4














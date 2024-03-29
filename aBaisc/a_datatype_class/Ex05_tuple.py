"""
#----------------------------------------------------------
[튜플 자료형]
    1- 리스트와 유사하지만 튜플은 값을 변경 못한다.
    2- 각 값에 대해 인덱스가 부여
    3- 변경 불가능 (*****)
    4- 소괄호 () 사용 ( 리스트[] )
"""


# (1) 튜플 생성
print('------------------- 1. 튜플 생성-----------------')
t = (1,2,3)
print(t)
print(t[0])

t2 = 1,2,3
print(t2) #(1, 2, 3)
print(t is t2) # true

# 빈 튜플 생성
# a = ()
a = ()
print(a)
print(type(a))


# (2) 튜플은 요소를 변경하거나 삭제 안됨
# t[1] = 0;  # 블럭이 생기면서 실행 안됨
# print(t)
# del t[1]   # 에러 발생
# print(t)

#del t # 튜플 통째로 삭제

print('------------------- 2 -----------------')


# (3) 'A'의 요소를 가진 튜플 t3을 선언하고 출력
print('------------------- 3 -----------------')
t3 =('A',) # 한개인 경우 ,추가 해줘야함
print(t3)

# (4) 인덱싱과 연산자
print('------------------- 4 -----------------')
print(t[2])
print(t[2:])
print(t*3)
print(t+t2)


#(5) 튜플 요소 풀기
print('------------------- 5 -----------------')
t5=(1,2,3)
a,b,c = t5
print(a+b)
"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
"""
'''
name = input('이름은?')
print('당신은 {0}입니다.'.format(name))
print('당신은 %s입니다.'%name)

# 나이를 입력받아서 한 살을 더해서 출력하기
age = int(input('나이는?'))
print('당신은  {0}살 입니다.'.format(age+1))
print('내년에는 %d살 입니다.' % (age+1))
'''


#사용자로부터 5개의 숫자를 읽어서 리스트에 저장하고 숫자들의 평균을 계산하여 출력한다.  또 숫자 중에서 평균을 상회하는 숫자가몇 개나 되는지 출력하여 보자.

a=[]
a.append(int(input("정수를 입력하세요")))
a.append(int(input("정수를 입력하세요")))
a.append(int(input("정수를 입력하세요")))
a.append(int(input("정수를 입력하세요")))
a.append(int(input("정수를 입력하세요")))
print(a)


avg_a=sum(a)/len(a)
print('평균:',avg_a)
sum = 0
for i in a:
    if(i > avg_a):
        sum +=1
print(sum)
a.reverse()
print(a)

import numpy
print(numpy.std(a))

#전화 키패드에는 각 숫자키마다 3개의 문자가 적혀있다. 사용자가입력한 문자열을 전화기의 숫자키로 변환하는 프로그램을 작성해보자
tel_list = {'ABC':2,'DEF':3,'GHI':4,'JKL':5,'MNO':6,'PQRS':7,'TUV':8,'WXYZ':9}
print(tel_list.keys())
b=[]
num=input("문자열을 입력하시오")
for i in num :
    for j in tel_list.keys():
        if j.__contains__(i):
           print(tel_list.get(j),end="")

print()

print("="*100)

#----------------------------------
# 단을 입력받아 구구단을 구하기
num = int(input("단을 입력하세요"))

for i in range(1,10):
    print('{0}X{1}={2}'.format(num,i,num*i))

#-----------------------------------------
# print() 함수



# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python Ex09_stdio.py ourserver scott tiger
#                                   0         1      2      3

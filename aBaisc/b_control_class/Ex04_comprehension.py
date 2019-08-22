"""
    @ 컴프리핸션 (comprehension)
    ` 하나 이상의 이터레이터로부터 파이썬 자료구조를 만드는 컴팩트한 방법
    ` 비교적 간단한 구문으로 반복문과 조건 테스트를 결합

    * 리스트 컨프리핸션
        [ 표현식 for 항목 in 순회가능객체 ]
        [ 표현식 for 항목 in 순회가능객체 if 조건 ]

    * 딕셔러리 컨프리핸션
        { 키_표현식: 값_표현식 for 표현식 in 순회가능객체 }

    * 셋 컨프리핸션
        { 표현식 for 표현식 in 순회가능객체 }

"""

'''
# 컨프리핸션 사용하지 않은 리스트 생성
alist = []
alist.append(1)
alist.append(2)
alist.append(3)
alist.append(4)
alist.append(5)
alist.append(6)
print(alist)

alist = []
for n in range(1,6):
    alist.append(n)
print(alist)

alist = list(range(1,6))
print(alist)

'''
#------------------------------------------------
# 리스트 컨프리핸션
# [예] [1,2,3,4,5,6]
blist = [n**3 for n in range(1,7)]
print(blist)

clist = [n for n in range(1,11,2)]
print(clist)

clist = [n for n in range(1,11) if n%2 ==0]
print(clist)

rows = range(1,4)
cols = range(1,7,2)

dlist=[(r,c) for r in rows for c in cols]
print(dlist)

#dlist에서 각 요소 추출하여 출력

for d in dlist:
    print(d)

for r2,c2 in dlist:
    print(r2,c2)

#-------------------------------------------
# 딕셔러니 컨프리핸션
# { 키 : 값 }

a = {x : x**2 for x in(2,3,4)}
print(a)

word = 'LOVE LOL'
wcnt = { letter: word.count(letter) for letter in word}
print(wcnt)

#------------------------------------------------
# 셋 컨프리핸션

aset = { n for n in range(1,7)}
print(aset)


alist = [ n for n in range(1,7) ]
print(alist)

#리스트 컨프리핸션과 셋 컴프리핸션의 차이.
'''

리스트 : 인덱스 /중복허용 /변경가능
튜플 : 인덱스 / 중복허용 /변경불가
셋 : 인덱스 x / 중복 x / 변경가능
딕셔너리 : 키와 밸류 / 키는 중복 x / 인덱스 x]


'''
data = [1,2,3,1,3,5,6,2]
aset = { n for n in data}
print(aset)

data = [1,2,3,1,3,5,6,2]
alist = [ n for n in data if n%2 ==1 ]
print(alist)



# -------------------------------------------------
# [참고] 제너레이터 컨프리핸션
# ( ) 를 사용하면 튜플이라 생각하지만 튜플은 컨프리핸션이 없다.
# 제너레이터 컨프리핸션은 한번만 실행
# 즉석에서 그 값을 생성하고 이터레이터를 통해 한번에 값을 하나씩 처리하고 저장하지 않음


data = [1,2,3,1,3,5,6,2]
alist = (n for n in data if n%2 ==1 ) # 제너레이터 컨프리핸션 ( 튜플아님)
print(alist)
print(list(alist)) #[1, 3, 1, 3, 5]

print('*'*40)
print(list(alist)) #[]

'''
#BMI(Body Mass Index)는 체중(kg)을 신장(m)의 제곱(**2)으로나눈 값으로
#체지방 축적을 잘 반영하기 때문에 비만도 판정에 많이 사용한다.
# 사용자로부터 신장과 체중을입력 받아서 BMI 값에 따라서 다음과 같은 메시지를 출력하는 프로그램을 작성하여 보자.

weight = int(input("무게(킬로그램)"))
height =float(input("키(미터)"))
bmi = weight/(height**2)
print("당신의 BMI:%.2f" %bmi)
if bmi >= 20 and bmi <25:
    print("정상입니다")
elif bmi >= 25 and bmi <29.9:
    print("과체중입니다")
elif bmi >= 30:
    print("비만입니다")

#2. 1부터 99까지 2자리의 정수로 이루어진 복권이 있다고 하자. 2자리가 전부 일치하면 1등상 100만원을 받는다.
# 2자리중에서 하나만 일치하면 50만원을 받고 하나도 일치하지 않으면 상금은 없다

import random
number =str(random.randint(1,100))
print(number)
in_num = input("복권번호(1-99사이)를 입력하시오")

if len(in_num)==1:
    count = 1
else:
    count=0

for n in range(len(in_num)):
    if in_num[n] == number[n]:
        count +=1
if count == 1:
    print("상금 50만원을 획득했습니다")
elif count == 2:
    print("상금 100만원을 획득했습니다.")
else:
    print("실패하셨습니다.")




'''

list_1 = [0, 3, 1, 7, 5, 0, 5, 8, 0, 4]
def quiz_2(list_data):

    a = set(list_data)
    print(a)
    return (list(a)[1:5])

print(quiz_2(list_1))


def delete_a_list_element(list_data, element_value):
    if element_value in list_data:
        list_data.remove(element_value)
        return list_data

    else:
        return "False"

list_data = ['a', 1, 'gachon', '2016.0']
element = float(2016)
result = delete_a_list_element(list_data, element)
print(result)



a = [3, "apple", 2016, 4]
b = a.pop(0)
c = a.pop(1)
print(b + c)



tuple_1 = (1, 2, 3)

tuple_2 = (4, 5, 6)

def quiz_1(data_1, data_2):
    result = []
    for i in (tuple_1 + tuple_2):
        result.append(i)
    return (result)
print(quiz_1(tuple_1, tuple_2))


dict_1 = {2:1, 4:2, 6:3, 8:4, 10:6}
dict_keys = list(dict_1.keys())
dict_values = list(dict_1.values())
dict_2 = dict()
for i in range(len(dict_keys)):
    dict_2[dict_values[i]] = dict_keys[i]
    print(dict_values[i])
print(dict_2)
print(dict_2[2])



animal = ['cat', 'snake', 'monkey', 'ant', 'spider']
legs= [4, 0, 2, 4, 8]
animal_legs_dict = {}
for i in range(len(animal)):
    animal_legs_dict[legs[i]] = animal[i]
    animal_legs_dict['ant'] = 6
print(animal_legs_dict)



Mydict = {'1' : 1, '2' : 2}
Copy = Mydict
print(Copy)
Mydict['1'] = 5
print(Copy)
result= Mydict['1'] + Copy['1']
print(result)


a = list(range(10))
print(a)
a.append(a[3])
print(a)
a.pop(a[3])
print(a)
a.insert(3, a[-1])
print(a)
a.pop( )
print(a)
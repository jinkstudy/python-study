"""
    collections 모듈: 파이썬의 내장 모듈
    (1) deque : 스택과 큐를 모두 지원하는 모듈
    (2) OrderedDict : 순서를 가진 딕셔러니 객체
    (3) defaultdict : 딕셔너리 변수를 생성할 때 키에 대한 기본 값을 지정
                  같은 이름의 키의 값을 하나로 만들 때 사용
    (4) Counter : 시퀀스 자료형의 데이터 값의 개수를 딕셔너리 형태로 반환하는 자료구조
    (5) namedtuple : 튜플의 형태로 데이터 구조체를 저장하는 방법
"""

#-------------------------------------
# (1) deque : 스택과 큐를 모두 지원하는 모듈
#           - 리스트와 비슷한 형식으로 데이타를 저장한다.
#           - append() 함수로 기존 리스트처럼 데이터가 인덱스 번호와 저장된다

from collections import deque

deque_list = deque()
for i in range(5): #0,1,2,3,4
    deque_list.append(i)
deque_list.pop() #stack처럼 4
deque_list.pop() #3
deque_list.insert(1,99)
print(deque_list) # deque([0, 99, 1, 2])





# -------------------------------------------
# (2) OrderedDict 모듈 : 순서를 가진 딕셔러니 객체
#                기본적인 딕셔너리는 순서를 보장하지 않는 객체이다

d = {} # 빈 딕셔너리 생성
d['z']=100
d['b']=200
d['s']=300
d['a']=400

for i in d.items():
    print(i)

for k,v in d.items():
    print(k,v)

from collections import OrderedDict

d = {} # 빈 딕셔너리 생성
d['z']=100
d['b']=200
d['s']=300
d['a']=400

for i in d.items():
    print(i)

for k,v in d.items():
    print(k,v)




#----------------------------------------------
# (3) defaultdict : 딕셔너리 변수를 생성할 때 키에 대한 기본 값을 지정
#                   같은 이름의 키의 값을 하나로 만들 때 사용
d=dict()  #d={} 와 같음
#print(d['first'])  #KeyError: 'first'
#[에러발생] - 생성하지 않은 키를 호출


from collections import defaultdict
d = defaultdict(lambda : 0) #lambda뒤에 아무 인자 쓰지 않으면 어떤것이 들어오더라도!  : 뒤를 반환하겠다 라는 의미!
print(d.items()) #dict_items([])
print(d['first'])  # key값이 없어도 에러발생하지 않고 0을 반환함
print(d.items()) #dict_items([('first', 0)])


s =[('yellow',1),('blue',2),('red',5),('yellow',3),('blue',2)]
d = defaultdict(list) # 초기값 형태를 list 구조로 하겠다.
print(d.items())  #dict_items([])
for k,v in s:
    d[k].append(v) #dict_items([('yellow', [1, 3]), ('blue', [2, 2]), ('red', [5])])
print(d.items())





#---------------------------------------------------
# (4) Counter 모듈 : 시퀀스 자료형의 데이터 값의 개수를 딕셔너리 형태로 반환하는 자료구조

from collections import Counter
text = list('gooooooooooooooood')
c = Counter(text) #Counter({'o': 16, 'g': 1, 'd': 1})
print(c)


# 딕셔너리 형식의 초깃값이 들어올 때
c = Counter({'yellow':5,'red':2})
print(c) #Counter({'yellow': 5, 'red': 2})
for a in c.elements():
    print(a)
print(list(c.elements())) #['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'red', 'red']

# 딕셔너리 외
c = Counter(yellow=5)
print(c) #Counter({'yellow': 5})

c = Counter('yellow=5')
print(c) #Counter({'l': 2, 'y': 1, 'e': 1, 'o': 1, 'w': 1, '=': 1, '5': 1})


#-------------------------------------------------
# (5) namedtuple : 튜플의 형태로 데이터 구조체를 저장하는 방법

from collections import namedtuple

Mypoint = namedtuple('MyPoint',['x','y'])
p = Mypoint(100,200)
print(p.x,p.y)
print(p.x + p.y)
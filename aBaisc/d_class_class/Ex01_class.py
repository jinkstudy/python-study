"""
     1) 클래스 기초

     ` __init__ 함수 : 객체 초기화 함수( 생성자 역할 )
     ` self : 객체 자신을 가리킨다.
"""

class Sample:
    # 멤버변수  초기화를 위래 생성자를 반드시 만들어야한다.

    def __init__(self): #생성자 함수
        self.name = '홍길동'
        self.age = 25
        address = "서울"
        print('생성자 호출')

    def __del__(self):
        print('소멸자 호출')

# 클래스 생성 - instance

a = Sample()
print(a.name)
print(a.age)
#print(a.address) --에러
del a



















"""
    2) 
    인스턴스 함수 :  'self'인 인스턴스를 인자로 받고 인스턴스 변수와 같이 하나의 인스턴스에만 한정된 데이터를 생성, 변경, 참조
    클래스   함수 :  'cls'인 클래스를 인자로 받고 모든 인스턴스가 공유하는 클래스 변수와 같은 데이터를 생성, 변경 또는 참조
    static  함수 :  클래스명 접근을 하며 객체끼리의 공유하고자 하는 메소드
    
    - 클래스 함수와 스태틱 함수는 둘 다 클래스명 접근
    - 클래스 함수는 cls를 이용하여 객체를 이용할 수 있다

"""

class Staff:
    cnt = 0
    def __init__(self,name):
        self.name = name

    #일반함수 (인스턴스 함수)
    def output(self):

        print('{0}님은 우리 직원입니다.'.format(self.name))

    @classmethod
    def output3(cls):
        cls.cnt += 1
        print('총 인원:', cls.cnt)


    @classmethod
    def step2(cls, name):
        print('222 우리회사는 사원, 직원, 책임으로 구성되어 있습니다.')
        print(name + "님은 222책임입니다.")
        return cls(name)

'''
    #static 함수 -->클래스명으로 접근 가능
    @staticmethod
    def step(name):

        print('우리회사는 사원, 직원, 책임으로 구성되어 있습니다.')
        print(name+"님은 책임입니다.")
'''
'''
    @staticmethod
    def output2(self):
        self.cnt +=1
        print('총 인원:',self.cnt)
'''





s2 = Staff('홍길자')
s2.output() #홍길자님은 우리 직원입니다.
s2.output3()
print("*"*50)

s2.output()
s2.output3()
#우리회사는 사원, 직원, 책임으로 구성되어 있습니다.
#홍길동님은 책임입니다.
#홍길자님은 우리 직원입니다.

print("*"*50)

s2.output()

#우리회사는 사원, 직원, 책임으로 구성되어 있습니다.
#홍홍이님은 책임입니다.
#홍길자님은 우리 직원입니다.

print("*"*50)
Staff.step2('콩콩이')
s2.output()




'''
     3) 클래스 상속
        - 파이션은 method overring은 있지만 method overloading 개념은 없다
        - 파이션은 다중상속이 가능
        - 부모 클래스가 2개 이상인 경우 먼저 기술한 부모클래스에서 먼저 우선 해당 멤버를 찾음
'''



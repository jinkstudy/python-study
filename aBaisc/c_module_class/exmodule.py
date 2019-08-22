'''exmodule.py
    sum() 함수 정의
        - 인자 2개를 받아서 더한 값을 리턴하는 함수
        - 두개의 인자가 다른 자료형이면 "자료형이 달라서 계산할 수 없음" 출력
        - 두 개의 인자가 같은 자료형일 경우만 더한 값을 리턴
'''

def sum(num1, num2):
    if(type(num1)==type(num2)):
        return num1 + num2
    else:
        return "자료형이 달라서 계산 할 수 없습니다."

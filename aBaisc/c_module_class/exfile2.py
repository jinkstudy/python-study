'''
exfile2.py
mypackage 안에 있는 mymodule을 임포트하여 사용하고자 함

'''
print("+"*50)
import mypackage.mymodule
print("+"*50)
today = mypackage.mymodule.get_weather()

print(today)

print("+"*50)
from mypackage import mymodule
print("+"*50)
#get_weather() 호출하여 출력
today = mymodule.get_weather()
print(today)


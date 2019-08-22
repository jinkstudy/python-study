'''
exfile3.py
    mypackage /exam /exmodule.py 안에 sum() 호출

'''


import exam.exmodule
print("*"*40)
print(exam.exmodule.sum(2,3))
print("*"*40)
from exam.exmodule import sum
print(sum(3,'4'))
print("*"*40)
from exam import exmodule
print(exmodule.sum(3,4))
print("*"*40)





"""
# Path는 파일 시스템에 접근하기 때문에, 기본적으로 운영체제 상에 조작 대상 파일 경로가 존재해야 합니다.
# PurePath는 순수 경로의 기반 클래스입니다.
# 파일 시스템에 접근하지 않기 때문에, 운영체제 상에 존재하지 않는 파일 경로를 다룰 수도 있습니다.
"""

#-------------------------------------------------------------------
# 1 - 존재하지 않는 파일
from pathlib import PurePath
#p = PurePath('a:/babo/myclass/myjob') #(경로 표시 할때 / \둘다 먹힘)
p = PurePath('\\192.168.0.45\Share\myjob') #원격이나, 경로만으로 작업이 필요할때 사용.



#-------------------------------------------------------------------
# 2. 실제 경로로 아닌 가짜 경로를 관리하는 PurePath를 어디에 사용할까?
# 아마도 경로나 파일명만 조작할 때 사용하지 않을까?
# 해당 경로나 파일명이 현재 컴퓨터가 아니기에 이름만 관리하는 작업이 필요할 듯 싶다

print(p.parts) #('a:\\', 'babo', 'myclass', 'myjob')
print(p.drive) #a:


#3. 경로 붙이기

p = PurePath('mywork')
c = p / 'python' / 'myclass'
print(c)

d=p.joinpath('java','ourjo','best')
print(d)

subdir = ('python','java','c')
e=p.joinpath(*subdir)
print(e)


#(4) 부모 경로 찾기

p = PurePath('C:/Windows/System32/drivers/etc/hosts')
print(p.parts) #('C:\\', 'Windows', 'System32', 'drivers', 'etc', 'hosts')
print(p.parts[3]) #drivers
print(p.parts[5]) #hosts
\
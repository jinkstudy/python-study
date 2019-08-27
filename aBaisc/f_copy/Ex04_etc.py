"""
경로 이동은  Path 모듈로 안되어 os 모듈이 필요하다
"""


from pathlib import Path
import os

#경로 변경
#print(Path.cwd()) #D:\mywork\git_python\aBaisc\f_system_class
#os.chdir('..')
#print(Path.cwd()) #D:\mywork\git_python\aBaisc

#print(Path.cwd()) #D:\mywork\git_python\aBaisc
#os.chdir('C:\Windows')
#print(Path.cwd()) #C:\Windows

print(os.environ["HOMEPATH"]) # 윈도우 경우 #\Users\Playdata
sub = Path('hadoop/myproject/myjob')
path = Path(os.environ["HOMEPATH"],sub)
print(path) #\Users\Playdata\hadoop\myproject\myjob


#---------------------------------

import shutil

#shutil.rmtree('imsi') #폴더안에 파일이 있어도 폴더 삭제 가능
#shutil.copy('Ex00.txt',Path('copy.txt'))

shutil.copytree('.','../f_copy') #현재 디렉토리를 통으로 copy


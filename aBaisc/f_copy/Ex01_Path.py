"""
 - import pathlib 만 선언하면
        Path클래스 사용시 pathlib.Path라고 명시해야 한다. 
"""
from pathlib import Path


# (1) 해당 경로와 하위 목록들 확인
#p = Path('C:\Windows')
p=Path('.') #현재경로 찾아줌
print(p)
print(p.resolve()) #D:\mywork\git_python\aBaisc\f_system_class

p=Path('..') #부모경로 찾아줌
print(p)
print(p.resolve()) #D:\mywork\git_python\aBaisc


result = []
for x in p.iterdir(): # 부모경로 기준 하위 dir 및 폴더 보여줌.
    if x.is_dir(): #자식이 폴더인 경우만.
        result.append(x)
print(result) #[WindowsPath('../a_datatype_class'), WindowsPath('../b_control_class'), WindowsPath('../c_module_class'), WindowsPath('../d_class

#Comprehension으로 표현.
result = [x for x in p.iterdir()]
print(result)

result1 = [x for x in p.iterdir() if x.is_dir()]
print(result1)

#(2) glob()이용

sub = list(p.glob('**/*.py')) #자손디렉토리 중에서 .py 찾기
print(sub)


#자손디렉토리 중에서 data 디렉토리 안에 csv파일만 찾기

sub = list(p.glob('**/data/*.csv')) #[WindowsPath('../e_file_class/data/imsi.csv')]
print(sub)

#(2) 파일시스템에 해당 파일이 존재하는지 여부


# (3) 윈도우는 경로 구분자로 역슬래쉬를 사용하지만 Path를 사용하면 슬래쉬로도 인식하여
# 운영체제의 영향없이 추상화하여 path를 사용할 수 있다


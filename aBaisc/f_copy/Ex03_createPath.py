from pathlib import Path

# ------------------------------------------------
# 1. 경로의 상태보기
print(Path.cwd())
print(Path.home()) #윈도우 C:/Users/계정명 리눅스(hadoop) : /home/hadoop/


p = Path('Ex03_createPath.py')
print(p.stat())
# ----------------------------------------------------
# 2. 경로(파일) 생성시간 알아보기
import stat
import datetime
p = Path('Ex03_createPath.py')
print(p.stat()[stat.ST_CTIME])
print(datetime.datetime.fromtimestamp(p.stat()[stat.ST_CTIME]))

# ------------------------------------------------
# 3. 디렉토리 생성
'''
p2 = Path('imsi')
p2.mkdir(exist_ok=True) #이미 있어도 만들겠다

p3 = Path('imsi2/myclass/python')
p3.mkdir(parents=True)
'''
# ------------------------------------------------
# 4. 파일 생성 -->open(w모드)
#  imsi/ a.txt 파일에 '홍길동 화이팅' 쓰기.

with open('imsi/a.txt','wt',encoding='utf-8') as f:
    f.write('홍길동 화이팅')
p = Path('imsi/b.txt')
with open(p,'wt',encoding='utf-8') as f:
    f.write('홍길동 화이팅')

p=Path('imsi/z.txt')
p.touch() #존재하지 않는 경로에도 파일을 만들어줌


#a.txt 파일명을 test.txt 파일명으로 변경
import os
os.rename('imsi/b.txt','imsi/test.txt')

os.replace('imsi/test.txt','imsi/test1.txt') #덮어쓰기됨.



# ------------------------------------------------
#  5. 경로 제거


f = Path('imsi')
#f.rmdir()  #디렉터리가 비어 있지 않습니다: 'imsi'

#파일 지우기 (imsi/z.txt 지우기)
f = Path('imsi/z.txt')
os.remove(f)

f = Path('imsi/test1.txt')
f.unlink()


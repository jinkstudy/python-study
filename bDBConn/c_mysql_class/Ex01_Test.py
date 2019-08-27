'''
files/emp.csv의 데이터들을 mysql emp테이블에 입력.
'''

import MySQLdb
import csv

def insertdata(db,data):
    conn = MySQLdb.connect(host='localhost',user='scott',passwd='tiger',db=db)
    cur = conn.cursor()
    sql = '''INSERT INTO emp(empno,ename,job,mgr,hiredate,sal,comm,deptno) 
                VALUES(?,?,?,?,?,?,?,?)'''

    data_tuple = tuple(data)

    cur.execute(sql, data_tuple)  # 입력값은 튜플 형식으로
    conn.commit()
    conn.close()
'''
def viewdata(db,table):
    conn = MySQLdb.connect(host='localhost', user='scott', passwd='tiger', db=db)
    cur = conn.cursor()
    sql = "select * from {0}".format(table)
    cur.execute(sql)
    datas = cur.fetchall()
    for row in datas:
       print(row[0],end=" ")
    print()    
    cur.close()
    conn.close()
'''
#  csv파일을 읽어서 DB에 테이블 입력
file_name='../files/emp.csv'
file = csv.reader(open(file_name,'r'), delimiter=',')
header = next(file,None) #한 줄을 읽어서 아무일도 하지 않는다.
print(header)
for row in file:
    #print(row)
    insertdata('pythondb',row)


#mysql에 기존 scott/tiger 계정이 있어야함
#viewdata('pythondb','emp')

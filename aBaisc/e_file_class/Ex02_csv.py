#[1] 리스트 데이터를 csv파일에 저장한다.
import csv

data = [[1,'김','책임'],[2,'박','선임'],[3,'주','연구원']]
with open('./data/imsi.csv','wt',encoding='utf-8') as f:
    cout=csv.writer(f)
    cout.writerows(data)

# [2] csv 파일을 읽어서 리스트 변수 저장 출력
data1 = []
with open('./data/imsi.csv','rt',encoding='utf-8') as f:
    cin = csv.reader(f)
    data1 = [row for row in cin if row]
    print(data1)

print( data == data1)


import json

f = open('./data/temp.json','rt',encoding='utf-8')
json_data=f.read()
data = json.loads(json_data)
print(data) #{'박열': {'No': 1, 'Job': '선임'}, '김원봉': {'No': 2, 'Job': '주임'}, '이순신': {'No': 3, 'Job': '연구원'}}
print(type(data)) #<class 'dict'>


for item in data:
    print("*" * 50)
    print('1 name >', item)
    for i,a in enumerate(data[item].items()):
        print(i+2,a[0],'>',a[1])
    print("*" * 50)


        #print('2>번호', data[item]['No'])
        #print('3>직업', data[item]['Job'])
   # for val in data[item].keys():


'''
(1) 이름 : xxxx
    번호 : x
    직업 :xxxx
(2) with 구문에 예외처리로 수정
'''



f.close()
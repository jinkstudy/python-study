a = [0,1,2,3,4]
print(a[:3],a[:-3])  #[0, 1, 2] [0, 1]

a= [0,1,2,3,4]
print(a[::-1]) #[4, 3, 2, 1, 0]


first = ["egg", "salad", "bread", "soup", "canafe"]
second = ["fish", "lamb", "pork", "beef", "chicken"]
third = ["apple", "banana", "orange", "grape", "mango"]
order = [first, second, third]

john = [order[0][:-2],second[1::3],third[0]]
print(john) #[['egg', 'salad', 'bread'], ['lamb', 'chicken'], 'apple']
del john[2]
john.extend([order[2][0:1]])
print(john) #[['egg', 'salad', 'bread'], ['lamb', 'chicken'], ['apple']]


list_a = [3, 2, 1, 4]
list_b = list_a.sort() # none
print(list_a) #원본 변경되버림 [1, 2, 3, 4]
print(list_a,list_b) # [1, 2, 3, 4] None

#정렬된 값 반환 받기 위해서는 sorted 써야함 --원본에 영향 없음.
list_a = [3, 2, 1, 4]
list_b = sorted(list_a)
print(list_a,list_b) # [3, 2, 1, 4] [1, 2, 3, 4]



fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry', 'melon']
print(fruits[-3:], fruits[1::3])


num = [1, 2, 3, 4]
print(num * 2) #[1, 2, 3, 4, 1, 2, 3, 4]


a = [1, 2, 3, 5]
b = ['a', 'b', 'c','d','e']
a.append('g')
b.append(6)
print('g' in b, len(b))

list_a = ['Hankook', 'University', 'is', 'an', 'academic', 'institute', 'located', 'in', 'South Korea']
list_b=[ ]
for i in range(len(list_a)):
    if i % 2 != 1:

        list_b.append(list_a[i])

print(list_b)


admission_year = input("입학 연도를 입력하세요: ")
print(type(admission_year))

country = ["Korea", "Japan", "China"]
capital = ["Seoul", "Tokyo", "Beijing"]
index = [1, 2, 3]
country.append(capital)
country[3][1] = index[1:]
print(country) #'Korea', 'Japan', 'China', ['Seoul', [2, 3], 'Beijing']]

a = [5, 4, 3, 2, 1]
b = a
c = [5, 4, 3, 2, 1]
print(a is b) # true
print(a is b) # true

list_1 = [[1, 2], [3], [4, 5, 6]]
a,b,c = list_1
list_2 = a + b + c
print(list_2) #[1, 2, 3, 4, 5, 6]
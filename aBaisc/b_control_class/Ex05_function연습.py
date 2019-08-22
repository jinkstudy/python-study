#리스트를 인자로 받아 짝수만 갖는 리스트 반환하는 함수

def even_filter(input=[]):
    result = [n for n in input if n%2 ==0]
    return result

print(even_filter([1, 2, 4, 5, 8, 9, 10]))




#주어진 수가 소수인지 아닌지 판단하는 함수
def is_prime_number(num):
    for n in range(2,num):
        if num % n == 0:
            return str(num)+"은 소수가 아닙니다."
            break
        elif n == num-1:
            return str(num) + "은 소수입니다."

print(is_prime_number(60))
print(is_prime_number(61))


def count_vowel(name):
    sum = 0
    for n in name:
        if n in 'aeiou':
            sum+=1
    return name+"에 포함된 모음의 갯수는"+str(sum)+"개입니다."


print(count_vowel("pythonian"))



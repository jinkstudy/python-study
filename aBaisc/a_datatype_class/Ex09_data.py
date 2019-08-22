"""
import datetime
today = datetime.date.today();
print('today is ', today)
"""

from datetime import date
today = date.today();
print('today is ', today)
#년,월,일 따로 출력

print(today.year , "년")
print(today.month , "년")
print(today.day, "년")


#현재의 날짜와 시간 구하기
from datetime import datetime
current_time = datetime.today()
print(current_time)

#날짜 계산
from datetime import timedelta

today = date.today()
print('어제 :',today+timedelta(days=-1))

#내일
print('내일 :',today+timedelta(days=+1))

#7일전
print('7일전 :',today+timedelta(weeks=-1))

'''데이트형과 문자형 간에 변환'''

#날짜 출력 형식 (strftime()아용)
today = datetime.today()
print(today)
print(today.strftime('%Y %m %d'))
print(today.strftime('%m/%d/%Y %H:%M'))

#문자열로 날짜형식 변환(strptime()이용)
str = '2020-08-20 12:25:33'
mydate = datetime.strptime(str,'%Y-%m-%d %H:%M:%S')
print(mydate)
print(type(mydate))
print(mydate.strftime('%m/%d/%Y %H:%M'))

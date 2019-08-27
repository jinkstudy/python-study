"""
    전세계날씨제공 API : http://openweathermap.org

    1. 회원가입 : 메뉴 > Sign Up > 사용용도 : Education > 대충가입 (무료는 1번에 60번 호출 가능 )
    2. 개발자모드 : Sign In > API Keys 에서 내가 발급받은 키 (추가 키 가능)
    3. 발급받고 바로 지정 안됨 (시간소요)
"""
import requests
import json

# API 키를 지정합니다. 자신의 키로 변경해서 사용해주세요.
apikey = "0d3c5383667a9c068ddf5b7a1d88ce6e"

# 날씨를 확인할 도시 지정하기
cities = ["Seoul,KR", "Tokyo,JP", "Nice,FR"]


api = 'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}'
#k2c = lambda k : k-273.15

for cname in cities:
    url=api.format(city=cname,key=apikey)
    res = requests.get(url)
    #print(res.text)
    #print(type(res.text)) #<class 'str'>
    data = json.loads(res.text)
    #print(type(data)) #<class 'dict'>
    print(data)

    print('도시명:',data['name'])
    print('날씨:',data['weather'][0]['main'])
    print('최저온도:',data['main']['temp_min'])
    print('최고온도:',data['main']['temp_max'])
    print('습도:',data['main']['humidity'])
    print('기압:',data['main']['pressure'])
    print('*'*50)


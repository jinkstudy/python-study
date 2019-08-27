'''
    http://www.data.go.kr
            - 회원가입필수
            - 일반인증키 요청 ( 바로 받을 수 있고 자료요청시 바로 승인됨 )

    >  관광자원통계서비스  >  상세기능 > 유료관광지방문객수조회
    : 전국의 주요 유로관광지 방문객수를 조회하기 위한 서비스로서
    기간,지역, 관광지별 외국인 방문객수와 내국인 방문객수를 조회한다.

    의미있는 데이타를 추출하여 출력한다

'''



from urllib import request
from urllib import parse
import json

access_key = 'IV2iM5P1kI0MHEiFd4nBauHiRAOzgoa9ZRUrhvxanXwo9mmLOMYbfRYDn5QBAQEZE7Npqnax%2BEFr3iNsTs9jUQ%3D%3D'
url = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
queryParams = '?_type=json'
queryParams += '&serviceKey=' + access_key
queryParams += '&YM=' + '201201'
queryParams += '&SIDO=' + parse.quote('부산광역시')
queryParams += '&GUNGU=' + parse.quote('해운대구')
queryParams += '&RES_NM=' + parse.quote('부산시립미술관')

req = request.Request(url + queryParams)
res = request.urlopen(req)
returnData = res.read().decode('utf-8')
print(type(returnData)) #<class 'str'>

data = json.loads(returnData)
print(type(data)) #<class 'dict'>
print("*"*50)
print("구:",data['response']["body"]["items"]['item']['gungu'])
print("관광지:",data['response']["body"]["items"]['item']['resNm'])


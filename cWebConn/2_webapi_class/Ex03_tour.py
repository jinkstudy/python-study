from urllib import request
from urllib import parse
import datetime
import json
import math

"""  관광지 입장객 정보 획득을 위한 파라메터 설정하여 결과를 얻어오는 함수
       - 년도, 시도, 구군, 페이지번호, 한페이지결과수를 지정 """
def getTourPointVistor(yyyymm, sido, gungu, nPgaenum, nItems):
    # -----------------------------------------------------------
    access_key = 'IV2iM5P1kI0MHEiFd4nBauHiRAOzgoa9ZRUrhvxanXwo9mmLOMYbfRYDn5QBAQEZE7Npqnax%2BEFr3iNsTs9jUQ%3D%3D'
    url = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
    queryParams = '?_type=json'
    queryParams += '&serviceKey=' + access_key
    queryParams += '&YM=' + yyyymm
    queryParams += '&SIDO=' + parse.quote(sido)
    queryParams += '&GUNGU=' + parse.quote(gungu)
    queryParams += '&RES_NM='
    queryParams += '&pageNo=' +str(nPgaenum)
    queryParams += '&numOfRows=' + str(nItems)

    req = request.Request(url + queryParams)
    res = request.urlopen(req)
    returnData = res.read().decode('utf-8')
   # print(type(returnData))  # <class 'str'>

    jsonData = json.loads(returnData)
    return jsonData


''' 각 항목을 JSON 구조로 변경하고 추가하는 함수'''
def getTourPointData(item, yyyymm, jsonResult):
    print('getTourPointData 호출')
    addrCd = 0 if 'addrCd' not in item.keys() else item['addrCd']
    gungu = 0 if 'gungu' not in item.keys() else item['gungu']
    sido  = 0 if 'sido' not in item.keys() else item['sido']
    resNm = 0 if 'resNm' not in item.keys() else item['resNm']
    rnum = 0 if 'rnum' not in item.keys() else item['rnum']
    ForNum = 0 if 'ForNum' not in item.keys() else item['ForNum']
    NatNum = 0 if 'NatNum' not in item.keys() else item['NatNum']

    jsonResult.append({'yyyymm' : yyyymm,
                       'addrCd' : addrCd,          # 지역코드 ( 우편번호와 일치한다고 하는데 )
                       'sido': sido,                # 시도
                       'gungo' : gungu,             # 구군
                       'resNm' : resNm,             # 관광지명
                       'rnum' : rnum,               # 관광지에 고유하게 부여된 코드값
                       'ForNum' : ForNum,           # 외국인수
                       'NatNum' : NatNum})          # 내국인수


''' 추출할 변수 지정하고 필요한 함수 호출하여 결과 받는 메인 함수'''
def main():
    jsonResult = []    # 결과 저장 변수

    # 검색할 변수값 지정
    sido = '서울특별시'      # 시도
    gungu = ''               # 구군
    nPagenum = 1             # 페이지번호
    nTotal = 0
    nItems = 100              # 한 페이지의 레코드 수? 100개가 넘으면 다음 페이지로 넘어가도록
                              # sido가 경기도면 100개가 넘어가 페이지 처리가 필요하단다
    nStartYear = 2015         # 추출할 년도의 시작년도
    nEndYear = 2017           # 추출할 년도의 종료년도

    #-----------------------------------------------------------
    # 여기에 코딩하기
    for year in range(nStartYear,nEndYear) :
        for month in range(1,13) : #1~12
            yyyymm = '{0}{1:0>2}'.format(str(year),str(month)) #{1:0>2} 두자리 수이며, 앞자리가 모자라면 0을 채워라
            nPagenum = 1

            while True:
                jsonData = getTourPointVistor(yyyymm,sido,gungu,nPagenum,nItems)
                if jsonData['response']['header']['resultMsg'] =='OK':
                    nTotal = jsonData['response']['body']['totalCount']
                    if nTotal == 0: break
                    for item in jsonData['response']['body']['items']['item'] :
                        getTourPointData(item,yyyymm,jsonResult)
                    nPage = math.ceil(nTotal/100)
                    if nPagenum == nPage : break
                    nPagenum+=1

                   # print(jsonData['response']['body'])
                else :break

            with open('./data/%s_관광지입장정보_%d_%d.json' % (sido,nStartYear,nEndYear),'w',encoding='utf-8') as f:
                saveToJson=json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
                f.write(saveToJson)







    print('%s_관광지입장정보_%d_%d.json로 저장되었읍니다.'%(sido, nStartYear, nEndYear-1))


''' 프로그램 시작점 '''
if __name__ == '__main__':
    main()


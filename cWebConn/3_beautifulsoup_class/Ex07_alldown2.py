"""
    파일을 다운받고 저장하는 함수

     [참고] 파이썬 정규식 표현 : https://wikidocs.net/4308
"""
from bs4 import BeautifulSoup
from urllib import parse
from urllib import request
import os, time, re  # re : 정규식

def download_file(url):
    p=parse.urlparse(url)
    print('1-',p) #1- ParseResult(scheme='https', netloc='docs.python.org', path='/3.6/library/', params='', query='', fragment='')
    savepath = './'+p.netloc + p.path
    print('2-',savepath) #2- ./docs.python.org/3.6/library/

    # '/'로 끝나서 파일명이 없는 경우는 index.html붙여줌.
    if re.search('/$',savepath):
        savepath += 'index.html'
        print('3-',savepath) #3- ./docs.python.org/3.6/library/index.html

    # 해당경로에 파일이 있으면 다운받지 않고 리턴.
    if os.path.exists(savepath) :#해당 경로가 있다면!
        return savepath
    savedir = os.path.dirname(savepath)
    print('4-',savedir) #4- ./docs.python.org/3.6/library

    #해당경로에 디렉토리가 없으면 디렉토리 생성
    if not os.path.exists(savedir): #경로가 없으면
        os.makedirs(savedir) # 해당 폴더를 만들어라.

    try:
        request.urlretrieve(url,savepath) #해당 url의 내용을 savepath라는 이름으로 저장해주세요.
        time.sleep(1)
    except:
        print('download failed:',url)
        return None


if __name__ == '__main__':
    url = 'https://docs.python.org/3.6/library/'
    result = download_file(url)
    print(result)




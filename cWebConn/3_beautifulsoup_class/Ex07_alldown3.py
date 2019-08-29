"""
    파이썬은 파일하나를 모듈로 취급한다면 다른 파일의 함수를 복사하지 않고 바로 호출한다.

    [주의] import Ex07_alldown1 코드부터 에러발생하지만 실행은 됨

"""


from bs4 import BeautifulSoup
from urllib.parse import *
from urllib.request import *
import os, time, re

# 에러 발생해도 실행은됨
import Ex07_alldown1
import Ex07_alldown2


# 이미 처리한 파일인지 확인하기 위한 변수
proc_files = {}

# HTML을 분석하고 다운받는 함수
def analyze_html(url, root_url):
    # ------------------------------------------------------
    savepath = Ex07_alldown2.download_file(url)

    #없으면 return
    if savepath is None: return
    if savepath in proc_files :return
    proc_files[savepath] = True # 작업한 파일을 배열에 추가.
    #print(proc_files)

    f = open(savepath,"r",encoding='utf-8')
    html = f.read()
    links = Ex07_alldown1.enum_links(html,url)
    #print(links)

    for url_link in links:
        #url_link.find(root_url)가 없으면 -1뜸. if -1 = true이므로 처리 필요.
        if url_link.find(root_url) !=0 : continue
        if re.search(".html$",url_link):  # url_link에서 .html로 끝나는 것들을 찾아라.
            analyze_html(url_link,root_url) # 자기 자신 호출?
            continue
        Ex07_alldown2.download_file(url_link)

if __name__ == "__main__":
    # URL에 있는 모든 것 다운받기
    url = "https://docs.python.org/3.5/library/"
    analyze_html(url, url)




#import urllib.request
from urllib import request

url = 'http://www.google.com'
site = request.urlopen(url)
#print(site)

page = site.read()
print(page)
print('**'*30)
print(site.status)
print('**'*30)

headers = site.getheaders()
print(type(headers)) #<class 'list'>

print('**'*30)
for a in headers:
    print(a[0])
    print(a[1])
    print('**'*30)
print('**'*30)




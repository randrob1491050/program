#!python3

""" this scripts for auto login and post with REQUESTS """
__author__ = 'iBSD@siteop.me'

import requests

USERNAME = 'xxx'.encode('utf-8')
LOGINSUBMIT = '登录'.encode('utf-8')

payload = {
    'username': USERNAME,
    'password':'xxx',
    'refer': 'http://xxx.xxx.xxx.xxx/uchome/space.php?do=home',
    'loginsubmit':LOGINSUBMIT,
    'formhash': '6ca0b170'
}
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'en,en-US;q=0.8,zh;q=0.6,zh-CN;q=0.4',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded',
    'DNT':'1',
    'Host':'xxx.xxx.xxx.xxx',
    'Origin':'http://xxx.xxx.xxx.xxx',
    'Pragma':'no-cache',
    'Referer':'http://xxx.xxx.xxx.xxx/uchome/index.php',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

url1 = "http://xxx.xxx.xxx.xxx/uchome/do.php?ac=387539ef1f575eb9b9f3b03ab8b275d8"
url2 = "http://xxx.xxx.xxx.xxx/uchome/cp.php?ac=thank&view=all"
s = requests.Session()
result = s.post(url1, data=payload, headers=headers)
print(result.status_code)
#print(result.content.decode('utf-8'))

payload2 = {
    'message':'感谢',
    'addsubmit':'true',
    'formhash':'b061a73e'
}
headers2 = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'en,en-US;q=0.8,zh;q=0.6,zh-CN;q=0.4',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded',
    'DNT':'1',
    'Host':'xxx.xxx.xxx.xxx',
    'Origin':'http://xxx.xxx.xxx.xxx',
    'Pragma':'no-cache',
    'Referer':'http://xxx.xxx.xxx.xxx/uchome/space.php?uid=47&do=thank&view=all',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
result2 = s.post(url2, data=payload2, headers=headers2)
print(result2.status_code)







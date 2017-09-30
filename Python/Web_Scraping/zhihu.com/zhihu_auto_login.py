#!python3

""" this scripts for zhihu auto login   """
__author__ = 'iBSD@siteop.me'

import time
import requests
from bs4 import BeautifulSoup
from PIL import Image

HEADERS = {
    'Host':'www.zhihu.com',
    'Referer':'https://www.zhihu.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

session = requests.Session()

def get_captcha():
    t = str(int(time.time() * 1000))
    #print(t)
    img_url = 'https://www.zhihu.com/captcha.gif?r=' + t + '&type=login'
    r = session.get(img_url, headers=HEADERS)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
    IMG = Image.open('captcha.jpg')
    IMG.show()
    captcha = input("验证码：")
    return captcha

def get_xsrf():
    zhihu_url = 'https://www.zhihu.com'
    r = session.get(zhihu_url, headers=HEADERS)
    soup = BeautifulSoup(r.content, "html.parser")
    xsrf = soup.find('input', attrs={"name": "_xsrf"}).get("value")
    return xsrf

def get_login(email, password):
    ZHIHU_LOGIN_URL = "https://www.zhihu.com/login/email"
    PAYLOAD = {
    '_xsrf': get_xsrf(),
    'password': password,
    'captcha': get_captcha(),
    'email': email
    }
    ZHIHU_DATA = session.post(ZHIHU_LOGIN_URL, data=PAYLOAD, headers=HEADERS)
    #print(ZHIHU_DATA.status_code)
    login_code = ZHIHU_DATA.json()
    print(login_code['msg'])

if __name__ == '__main__':
    email = 'xxx'
    password = 'xxx'
    get_login(email, password)


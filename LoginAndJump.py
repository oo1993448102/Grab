# 登录所需post数据
import http.cookiejar
import os
import urllib

import re

login = {
}

header = {'Connection': 'Keep-Alive',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50',
          'Cache-Control': 'max-age=0',
          }

loginUrl = 'https://www.zhihu.com/login/phone_num'
mainUrl = 'https://www.zhihu.com/'

def makeOpener(head, cj=http.cookiejar.CookieJar()):
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

def save(data,fileName = 'out.html',mode = 'w+'):
    path = '/Users/scott_he/Documents/grab/'
    if not os.path.exists(path):
        os.mkdir(path)
    f_obj = open(path + fileName, mode)
    f_obj.write(data)
    f_obj.close()

name = input('账号:')
password = input('密码:')
login['password'] = password
login['phone_num'] = name

postData = urllib.parse.urlencode(login).encode()
op = makeOpener(header).open(loginUrl, postData)
data = makeOpener(header).open(mainUrl).read()\
    .decode('utf-8')
save(data)

# 头像匹配
linkRule = '(<img\ssrc=".+?"\s' \
           'class="zm-item-img-avatar">)'

for x in re.compile(linkRule).findall(data):  # 括号内
    print(x)
    save(x + '\n','avater.html','a+')


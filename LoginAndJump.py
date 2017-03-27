# 登录所需post数据
import http.cookiejar
import json
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
mainUrl = 'https://www.zhihu.com/question/35913647'


def makeOpener(head, cj=http.cookiejar.CookieJar()):
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


def save(data, fileName='out.html', mode='w+'):
    path = '/Users/scott_he/Documents/grab/'
    if not os.path.exists(path):
        os.mkdir(path)
    f_obj = open(path + fileName, mode)
    f_obj.write(data)
    f_obj.close()


def getLoginInfo():
    name = input('账号:')
    if len(name.strip()) == 0:  # 去空格后时候为空 没有更好的判断方法?
        name = '15800758995'
    password = input('密码:')
    if len(password.strip()) == 0:
    #可在此输入默认密码
        password = ''
    login['password'] = password
    login['phone_num'] = name


def goMainPage():
    getLoginInfo()
    postData = urllib.parse.urlencode(login).encode()
    op = makeOpener(header).open(loginUrl, postData)
    # json解析
    jsonStr = json.loads(op.read().decode('utf-8'))
    print(jsonStr['msg'])
    data = makeOpener(header).open(mainUrl).read() \
        .decode('utf-8')
    save(data)

    # 头像匹配
    # <img src="https://pic1.zhimg.com/da8e974dc_s.jpg" class="zm-item-img-avatar">
    linkRule = '(<img\ssrc=".+?"\s' \
            'class="zm-item-img-avatar">)'

    # 当前页面所有图像  [\s\S]*?可匹配任意字符  .*不能匹配换行符
    linkRule_2 = '(<img.+src=".+?"' \
                '[\s\S]*?>)'

    for x in re.compile(linkRule_2).findall(data):  # 括号内
        if re.search('class="zm-list-avatar avatar"',x) : #符合话题内头像规则   f
            print(x)
            # 替换小头像
            # replace = re.sub('_s','',x)
            # print(replace)
            save(x + '\n', 'avater.html', 'a+')

import http.cookiejar
import os
import re
import urllib

loginUrl = 'https://www.zhihu.com/login/phone_num'
mainUrl = 'https://www.zhihu.com/'

cookie = {
    'z_c0': 'Mi4wQUJCSzIwOWpBUWtBY0FKQWFUamJDaGNBQUFCaEFsVk5uMlR3V0FCZkpUOHFYRUI0OGlaUUdLVkpnLVBlWFZJeThR|1489557407|a0ad053ec8985b3e0e4066e357556c2bd8eaae50',
    'nweb_qa': 'heifetz'}

def dicString(dictionary):
    string = ''
    for key, value in dictionary.items():
        string += '{}={};'.format(key, value)
    return string[:-1]


header = {'Connection': 'Keep-Alive',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50',
          'Cache-Control': 'max-age=0',
          'Cookie': dicString(cookie)
          }


# 加入header 模仿浏览器
def makeOpener(head, cj=http.cookiejar.CookieJar()):
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


# 储存结果到本地
def save(data):
    path = '/Users/scott_he/Documents/grab'
    if not os.path.exists(path):
        os.mkdir(path)
    f_obj = open(path + '/out.html', 'w+')  # 打开方式 每次都重新记录 删除曾今
    f_obj.write(data)
    f_obj.close()


def saveAvater(data):
    path = '/Users/scott_he/Documents/grab'
    if not os.path.exists(path):
        os.mkdir(path)
    opt = open(path + '/avater.html', 'a+')
    opt.write(data)
    opt.close()


cj = http.cookiejar.CookieJar()
data = makeOpener(header, cj).open(loginUrl, timeout=2000).read() \
    .decode('utf-8')
# 头像匹配
linkRule = '(<img\ssrc=".+?"\s' \
           'class="zm-item-img-avatar">)'

for x in re.compile(linkRule).findall(data):  # 括号内
    print(x)
    saveAvater(x + '\n')
save(data)
for item in cj:
    print('{} = {}'.format(item.name, item.value))
print(cj)

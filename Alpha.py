import http.cookiejar
import os
import urllib.request
from collections import deque

import re

queue = deque()
visited = set()

# 加入header 模仿浏览器
def makeOpener(head = {'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'}):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key,value in head.items():
        elem = (key,value)
        header.append(elem)
    opener.addheaders = header
    return opener

# 储存结果到本地
def save(data):
    path ='/Users/scott_he/Documents/grab'
    if not os.path.exists(path):
        os.mkdir(path)
    f_obj = open(path+'/out.txt', 'a+')  # 打开方式  a+
    f_obj.write(data)
    f_obj.close()


opener = makeOpener()
url = "https://baidu.com"
queue.append(url)
cnt = 0

while queue:
    url = queue.popleft()
    if (url not in visited):
        visited.add(url)
        print('已经抓取' + str(cnt) + '正在抓取' + url+'队列数量'+str(len(queue)))
        cnt += 1
        # 纯属为了观察输出加的限制
        if cnt == 3:
            break

        try:
            # urlop = urllib.request.urlopen(url,timeout=2)
            urlop = opener.open(url,timeout=2)
        except:
            continue

        if 'html' not in urlop.getheader('Content-Type'):
            continue

        try:
            data = urlop.read().decode('utf-8')
        except:
            continue

        linkRule = 'href="(.+?)"'
        for x in re.compile(linkRule).findall(data):
            if re.match('http', x) and x not in visited:
                queue.append(x)
                print(x + '加入队列')
                save(x+' '+'队列数量'+str(len(queue))+'\n')
print('finish')

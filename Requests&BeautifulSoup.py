import json

import re
import requests
import time

from Util import *
from bs4 import BeautifulSoup

# 不填入header导致结果500
header = {'Connection': 'Keep-Alive',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50',
          'Cache-Control': 'max-age=0',
          }

cookie = {
    'z_c0': 'QUJCSzIwOWpBUWtYQUFBQVlRSlZUWXFJOFZnSFlXb2NaTF9iaWZvUGdCV3dqc0Z4WFh4eGVRPT0=|1489976060|241d214dea1a27f64cbd0c18d4474c929c48bd59',
    'nweb_qa': 'heifetz',
}

question_api = 'https://www.zhihu.com/api/v4/questions/35913647/answers'

needDefaultAvatar = False

def jumpNext(session, next_url):
    # 防止过快访问
    time.sleep(1)
    keepGet(session, session.get(next_url, headers=header, cookies=cookie).json())
    pass


def keepGet(session, response):
    for obj in response['data']:
        avatar_url = obj['author']['avatar_url']
        print(avatar_url)
        avatar_img = '<img src="{}">'.format(avatar_url) + '\n'
        if not needDefaultAvatar:
            default_avatar_rule = 'zhimg.com/.{9}_is.jpg'
            if re.search(default_avatar_rule,avatar_img):
                continue
            else:
                save(avatar_img, 'avatar.html', 'a+')
        else:
            save(avatar_img, 'avatar.html', 'a+')
    if (response['paging']['is_end']):
        pass
    else:
        next_url = response['paging']['next']
        jumpNext(session, next_url)
    pass


if __name__ == '__main__':

    # cookieStr = 'z_c0=Mi4wQUJCSzIwOWpBUWtBY0FKQWFUamJDaGNBQUFCaEFsVk5MVDRBV1FDNVBEdmw5RThQNEZ1UTdWeXRNNVoyQzByd0Fn|1490596171|c3d9f8544432968bfa067799bae8264639427124;  s-t=autocomplete;  _xsrf=5d37904d2b5fd45725bcfaface79112e;  _zap=036fa507-cd94-4baa-b6c4-b7bb3225253e;  l_n_c=1; _zap=38fc2748-65d4-4fb3-bd3e-df28adef941c;  r_cap_id="ZDk4NmIwNWQ2YjAwNGVhNDhjOTUwOWNjMzk3ODYzZDQ;  __utmz=51854390.1490176124.19.14.utmcsr;  cap_id="NjYxZWRhNjJhOWU0NDBmNGE1MjUyM2RlZGExNmQ2NGQ;  s-q=%E7%A7%81%E4%BA%BA%E5%BD%B1%E9%99%A2;  __utmc=51854390;  __utmv=51854390.100--|2;  _ga=GA1.2.1821535004.1486707402;  nweb_qa=heifetz;  aliyungf_tc=AQAAAO8p13EJ4AYAkmeotK2ipoZhJrJ1;  d_c0="AHACQGk42wqPTh3jpZOT29_kv2_B2d48ebs;  sid=4jj8s988;  __utma=51854390.1821535004.1486707402.1490347096.1490595755.22;  s-i=13;  q_c1=d945c412089743a486e7c05c2659edfc|1488862371000|1479290320000'
    # cookie = formatCookie(cookieStr)

    params = {'offset': 0,
              'limit': 20,
              'sort_by': 'default'
              }
    # session可用于cookie的自动保存
    session = requests.session()
    request = session.get(question_api, params=params, cookies=cookie, headers=header)
    # print(request.url)
    # json格式 最后一个参数用于utf-8保留
    response = json.dumps(request.json(), indent=4, ensure_ascii=False)
    if request.status_code == 200:
        print('success')
        # save(response,'json.html')
        keepGet(session, request.json())
    else:
        print(response)
    print('finish')

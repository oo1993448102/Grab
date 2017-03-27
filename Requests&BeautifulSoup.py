import requests
from bs4 import BeautifulSoup
from LoginAndJump import save

cookie = {
    'z_c0': 'QUJCSzIwOWpBUWtYQUFBQVlRSlZUWXFJOFZnSFlXb2NaTF9iaWZvUGdCV3dqc0Z4WFh4eGVRPT0=|1489976060|241d214dea1a27f64cbd0c18d4474c929c48bd59',
    'nweb_qa': 'heifetz',
}


# 不填入header导致结果500
header = {'Connection': 'Keep-Alive',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50',
          'Cache-Control': 'max-age=0',
          }


question_url = 'https://www.zhihu.com/question/35913647'
request = requests.get(question_url,headers = header,cookies = cookie)
# response = BeautifulSoup(request.text)
# print(request.text)
print(request.text)
# save(response)

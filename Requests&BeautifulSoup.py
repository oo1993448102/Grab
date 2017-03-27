import requests
from bs4 import BeautifulSoup
from LoginAndJump import save

cookie = {
    'z_c0': 'QUJCSzIwOWpBUWtYQUFBQVlRSlZUWXFJOFZnSFlXb2NaTF9iaWZvUGdCV3dqc0Z4WFh4eGVRPT0=|1489976060|241d214dea1a27f64cbd0c18d4474c929c48bd59',
    'nweb_qa': 'heifetz',
}


question_url = 'https://www.zhihu.com/question/35913647'
request = requests.get(question_url,cookies = cookie)
response = BeautifulSoup(request.text)
# print(request.text)
print(response)
save(response)

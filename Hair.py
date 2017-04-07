import json

import re
import requests
from bs4 import BeautifulSoup
from Util import *

header = {'Connection': 'Keep-Alive',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) '
                        'AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50',
          'Cache-Control': 'max-age=0',
          }

cookie = {
    'z_c0': 'QUJCSzIwOWpBUWtYQUFBQVlRSlZUWXFJOFZnSFlXb2NaTF9iaWZvUGdCV3dqc0Z4'
            'WFh4eGVRPT0=|1489976060|241d214dea1a27f64cbd0c18d4474c929c48bd59',
    'nweb_qa': 'heifetz',
}

params = {'offset': 0,
          'limit': 20,
          'sort_by': 'default',
          'include': 'data[*].is_normal,is_sticky,collapsed_by,suggest_edit,comment_'
                     'count,can_comment,content,editable_content,voteup_count,reshipment_'
                     'settings,comment_permission,mark_infos,created_time,updated_time,'
                     'relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,'
                     'upvoted_followees;data[*].author.is_blocking,is_blocked,is_followed,'
                     'voteup_count,message_thread_token,badge[?(type=best_answerer)].topics'
          }

base_url = 'https://www.zhihu.com'
origin_url = '/r/search?q=%E7%9F%AD%E5%8F%91&sort=upvote&type=content&offset=0'

visited = set()


def jumpNext(session, next_url, page):
    response = session.get(next_url, headers=header).json()
    page += 1
    goToQuestion(session, response, page)
    pass


def goToQuestion(session, response, page=1):
    print(page)
    for answer in response['data']:
        if (answer['voteup_count'] >= 500):
            content = answer['content']
            soup = BeautifulSoup(content, 'html.parser')
            rule = {
                'class': 'origin_image zh-lightbox-thumb',
            }
            imgs = soup.findAll('img', rule)
            # print(imgs)
            for img in imgs:
                print(img['src'])
                img_html = '<img src="{}"/>\n'.format(img['src'].replace('_b', '_l'))
                save(img_html, answer['question']['title'] + '.html', 'a+')
        else:
            continue
    # if (response['paging']['is_end']):
    #     pass
    # else:
    #     next_url = response['paging']['next']
    #     jumpNext(session, next_url, page)
    pass


def get_html(session, request):
    if request.status_code == 200:
        next_url = request.json()['paging']['next']
        if len(request.json()['htmls']) != 0:
            for li in request.json()['htmls']:
                soup = BeautifulSoup(li, "html.parser")
                rule = {
                    'class': 'js-title-link',
                    'target': '_blank'
                }
                href = soup.find('a', rule)['href']
                if href not in visited:
                    if re.match('/question', href):
                        visited.add(href)
                        hrefList = href.split('/')
                        question_url = base_url + '/api/v4/' + hrefList[1] + 's/' + hrefList[2] + '/answers'
                        response = session.get(question_url, params=params, headers=header).json()
                        goToQuestion(session, response)
        if (len(next_url) != 0):
            next_request = session.get(base_url + next_url, headers=header)
            get_html(session, next_request)



    else:
        print(str(request.status_code))
        pass
    pass


if __name__ == '__main__':
    session = requests.session()
    request = session.get(base_url + origin_url, cookies=cookie, headers=header)
    # response = json.dumps(request.json(), indent=4, ensure_ascii=False)
    get_html(session, request)
    print('finish')

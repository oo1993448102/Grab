import urllib.request
import urllib.parse


url = "http://en.wikipedia.org/w/index.php?"
path = {}
path['search'] = '框架'
path['title'] = 'Special:Search'
path['go'] = 'Go'
path['searchToken'] = 'bj1rw10ycowqyjmr992frroz6'
url_path = urllib.parse.urlencode(path)
url_final = url+url_path
print(url_final)
response = urllib.request.urlopen(url_final).read()
html = response.decode('UTF-8')
print(html)
# Grab
#### first try.python for web crawler

#### 练手  python入门及爬虫入门

* python入门

  [Class : 类与继承](https://github.com/oo1993448102/Grab/blob/master/Class.py)

  [Expection : 自定义异常及捕捉](https://github.com/oo1993448102/Grab/blob/master/Expection.py)

  [*Structure : 数据结构](https://github.com/oo1993448102/Grab/blob/master/Structure.py)
  
  [ZipFile : 文档压缩及存储 ](https://github.com/oo1993448102/Grab/blob/master/ZipFile.py)

* 爬虫入门
  
  [RegularRule : 正则表达式 re库](https://github.com/oo1993448102/Grab/blob/master/RegularRule.py)
  
  [Alpha : 以某网页为入口 简单的抓取url](https://github.com/oo1993448102/Grab/blob/master/Alpha.py)
  
  [GrabZhihu : 手动复制cookie登录 抓取头像](https://github.com/oo1993448102/Grab/blob/master/GrabZhiHu.py)
  
  [FinalTest : 入口 输入账号密码获取并保存cookie 静态页面头像抓取](https://github.com/oo1993448102/Grab/blob/master/FinalTest.py)
    
 * 爬虫实践
 
    [Hair](https://github.com/oo1993448102/Grab/blob/master/Hair.py)
    
    [Request&BeautifulSoup : 使用三方库实现快速查询](https://github.com/oo1993448102/Grab/blob/master/Requests%26BeautifulSoup.py)
    
  
 
 * Notes
  
   [BeautifulSoup文档](https://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html)
  
    [Requests文档](http://docs.python-requests.org/en/latest/user/quickstart/#make-a-request)
  
    [简单爬虫入门](http://jecvay.com/2015/02/python3-web-bug-series5.html)
    
* Final  

  实现了用python模仿知乎登录（urllib，requests）均可实现，后因登录次数过多，需要验证码，所以直接保存了cookie用以登录。对于静态页面的抓取可以用正则表达式或BeautifulSoup库进行匹配抓取合适内容（GrabZhihu、LoginAndJump中均有体现）,对于使用js动态加载的，需在分析api后直接对api进行访问，从返回的json中得到所需数据（可参考Request&BeautifulSoup）。最终实现了对于知乎[哪张照片让你不由地感叹「年轻，真好」](https://www.zhihu.com/question/35913647)下所有用户头像的抓取，没有保存在本地，仅以\<img/>形式保存下来([avatar.html](https://github.com/oo1993448102/Grab/blob/master/avatar.html))。
  
  实现了用python爬取知乎某关键字下下全部问题中点赞数过500（可修改）的回答中图片的抓取，同时配合mongoDB将结果存入数据库中。通用性较强，例中关键字为短发，需要修改为其他关键字的可抓包获取加载时api。


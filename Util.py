import os


# Cookie Str to Dictorinary
def formatCookie(cookieStr):
    cookieList = cookieStr.split(';')
    # print(cookieList)
    cookie = {}
    for str in cookieList:
        map = str.split('=')
        cookie[map[0]] = map[1]
    return cookie


# 保存到本地 数据 文件名 读写方式
def save(data, fileName='out.html', mode='w+'):
    path = '/Users/scott_he/Documents/grab/'
    if not os.path.exists(path):
        os.mkdir(path)
    f_obj = open(path + fileName, mode)
    f_obj.write(data)
    f_obj.close()

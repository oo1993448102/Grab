import re

tel = '010-12345678'
rule = '(\d{3}-)?\d{8}'

# 起始位置匹配 不然返回None
answer =re.match(rule,tel)

print(answer)
if answer:
    print('true')
    # group为分组 只有在括号中的才是group!!!后面可以用/1等代替 也可以另2取名
    print(answer.group())
    # 原字符串 从1开始计数
    print(answer.group(0))
    # 第一部分匹配的字符串
    print(answer.group(1))
    # print(answer.group(2))
else:
    print('false')

# 扫描整个字符串并返回第一个成功的匹配
search = re.search(rule,'000'+tel)

print(search.span())

#扫描并替换
replace = re.sub(rule,"这是电话号码","随便加点前缀:"+tel)
print(replace)

def change(matched):
    return matched.group(1)+"sss"
replace = re.sub(rule,change,tel) #可用函数
print(replace)


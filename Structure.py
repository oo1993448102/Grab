# List 列表
myList = ['1','2','3','4']
print(myList)

for item in myList:
    print(item)

myList.append('add')
print(myList)

print(myList[1])

del myList[len(myList)-1]
print(myList)

myList.sort()  #这玩意居然不带返回值???   难道括号内那种有返回 .方法那种是没有返回的??并不对!
print(myList)


# Tuple 元组
# 长度 内容不会改变 有点像Java数组

aTuple = ('1','2')
bTuple = ('3',aTuple)
single = ('4',)
empty = ()
print(bTuple)
print(bTuple[1][0])


# 字典  dictionary
d = {1:'a',2:'b','3':'c'}
print(d)
print(d[2],d['3'])
del d['3']

for name,address in d.items():
    print('{} with {}'.format(name,address))

d['4'] = 'd'
print(d)

# 序列
print(myList[:])
print(myList[:1])

# 集合 set{}
# sorted(myList)
bri = set(myList)
print(bri)  #无序的
bri.add('1') #不可重复
print(bri)
bri.add('5')
print(bri)
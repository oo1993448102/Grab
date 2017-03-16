# test
# print("hello world")
# name = "echo"
# print("{} is {}".format(name, age), end="asas")

# if age == guess :
#     print("success")
# else:
#     print("fail")



def testDef():
    age = 12
    running = True
    while running:
        guess = int(input("input a num : "))
        if age == guess:
            print("success")
            running = False
        else:
            print("fail")
    else:
        print("Done")
#
# testDef()


import sys
x = 50

def change():
    # 文档字符串 DocString
    # 该文档字符串所约定的是一串多行字符串，其中第一行以某一大写字母开始，以句号结束。 第二行为空行，后跟的第三行开始是任何详细的解释说明。5
    # 在此强烈建议你在有关你所有非
    # 凡功能的文档字符串中都遵循这一约定。
    '''sas

    a'''
    global x
    x = 2
    print(x)

change()
print(x)
# print(change.__doc__)
# help(change)
for i in sys.argv:
    print(i)

__version__ = '0.1'





# import logging
#
# # like try..catch..
# try:
#     text = input('Try now')
#     # 指明错误类型
# # except EOFError:
#     # print('EOFError')
#     # print('EOFError')
#
# # 未知错误类型
# except :
#     print('fail')
# else:
#     print(text)

# 自定义异常
import logging


class TooShortException(Exception):

    def __init__(self,description):
        self.description = description
        print(description)

try:
    text = input("Exception")
    if(len(text)<3):
        # 异常抛出
        raise TooShortException("too short")
except:
    print("raise")
else:
    print('success')
finally:
    print('always')

logging.info('logging')


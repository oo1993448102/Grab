class Member:

    # 此方法相当于构造器,但是只能有一个构造方法??
    def __init__(self,name):
        self.name = name

    def output(self):
        print(self.name,end=" ")


# 继承
class Teacher(Member):

    def __init__(self,name,pay):
        Member.__init__(self,name)
        self.pay = pay

    def output(self):
        Member.output(self)
        print(self.pay)

class Student(Member):
    def __init__(self,name,score):
        Member.__init__(self,name)
        self.score = score

# 重写父类方法,也可以直接运行父类方法,和java继承一样,但是super方法要自己声明
#     def output(self):
#         Member.output(self)
#         print(self.score)

t = Teacher("Teacher",30)
s = Student('Student',100)

t.output()
s.output()
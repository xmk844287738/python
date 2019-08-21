
'''
类属性、对象属性
'''
class Student(object):
    def __new__(cls, *args, **kwargs):
        print('我是NEW函数')    # 追踪 __new__ 函数的执行过程
        print(type(cls))
        return object.__new__(cls)  #调用父类的（object）的new方法，返回一个Student实例，这个实例传递给init的self参数

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('我是 __init__')    # 追踪 __init__ 函数的执行过程

    def study(self):
        print("我爱学习")


if __name__ ==  '__main__':
    s = Student('张三',20)
    # print(s.name)
    # print(s.age)
    # s.study()




# class Student:
#     def __init__(self,name,chinese,math,english):
#         self.name = name
#         self.chinese = chinese
#         self.math = math
#         self.english = english
#
#     def __repr__(self):
#         return "<Student:{},chinese:{},math:{},english:{}>".format(self.name,self.chinese,self.math,self.english)
#
#
# s1 = Student('小王',90,90,75)
# print(s1)


class Student:
    def __init__(self,name,chinese,math,english):
        self.name = name
        if 0<chinese<100:
            self.chinese = chinese
        else:
            raise ValueError("Valid value must be in [0, 100]")

        if 0<math<100:
            self.math = math
        else:
            raise ValueError("Valid value must be in [0, 100]")

        if 0<english<100:
            self.english = english
        else:
            raise ValueError("Valid value must be in [0, 100]")


    def __repr__(self):
        return "<Student:{},chinese:{},math:{},english:{}>".format(self.name,self.chinese,self.math,self.english)


# s1 = Student('小王',90,90,-75)
s1 = Student('小王',90,90,120)
print(s1)

''''类属性 对象属性'''

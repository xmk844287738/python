'''
生成器
'''
def fib():
    a,b = 0,1
    while True:
        yield a #yield a 语句可以使 fib()函数变成可迭代对象
        a,b = b,a+b

# g = fib()
# print(g)

def gen_ab():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')

# g2 = gen_ab()
#
# next(g2)
#
# next(g2)

# next(g2)

import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentenca1:
    # def __init__(self,text):
    #     self.text = text
    #     self.words = RE_WORD.finditer(text)
    #
    # def __iter__(self):
    #     for e in self.words:
    #         yield e.group()

    def __init__(self,text):
        self.text = text
    '''
    生成器函数
    '''
    def __iter__(self):
        # for e in RE_WORD.finditer(self.text):
        #     yield e.group()

        return (math.group() for math in RE_WORD.finditer(self.text))
s1 = Sentenca1("han leng zhang jia rui han leng zhang jia rui han leng zhang jia rui")

# s2 = RE_WORD.findall("han leng zhang jia rui han leng zhang jia rui han leng zhang jia rui")
# s3 = RE_WORD.finditer("han leng zhang jia rui han leng zhang jia rui han leng zhang jia rui")

# print(s2)
# print(s3)

# for e in s1:
#     print(e)



'''
生成器嵌套
'''
# def integer():  #产生整数生成器
#     for i in range(1,9):
#         yield i
integer =(i for i in range(1,8))    #简写方式

# g1 = integer()
# for g in g1:
#     print(g)

# def squared(seq):  #产生整数平方生成器
#     for i in seq:   # seq 为可迭代对象
#         yield i*i
squared = (i*i for i in integer)

# g1 = squared(integer())
#
# for g in g1:
#     print(g)

# def negated(seq):  #基于整数平方的生成器,产生负的整数平方生成器
#     for i in seq:   # seq 为可迭代对象
#         yield -i

negated = ( -i for i in squared)

g1 = negated(squared(integer()))
for g in g1:
    print(g)
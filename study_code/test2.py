'''
偏函数 partial      callable可调用对象
'''
from functools import partial

def spam(a,b,c,d):
    print(a,b,c,d)

# s1 = partial(spam,1) # a=1
# spam(1,2,3,4)
s1 = partial(spam,d=50) # d=50  *kwargs  关键字参数
s1(2,3,4)

import math
from functools import partial


points = [ (1, 2), (3, 4), (5, 6), (7, 8) ]

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)   #欧式距离,平面间两点公式

pt = (4,3)
points.sort(key=partial(distance,pt))   #sort 默认升序排序,points.sort(key=partial(distance,pt)) 此做法改变 points列表中原有的数据排序，没有生产新的列表集合
print(points)


# def test1():
#     print("1")
#     print("2")
#
# def test2():
#     print("3")
#     print("4")
#
# # a = test1()
# # b = test2()
# print(test1)
# print(test2)

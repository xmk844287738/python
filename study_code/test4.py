'''
生成器函数2
'''
# import inspect
#
# def echo(value=None):
#     print("---Execution starts when 'next()' is called for the first time.---")
#
#     try:
#         while True:
#             try:
#                 value = yield value
#             except Exception as e:
#                 value = e
#
#     finally:
#         print("---Don't forget to clean up when 'close()' is called.---")
#
# g2 = echo()
# print(inspect.getgeneratorstate(g2))
# print(next(g2))
# print(inspect.getgeneratorstate(g2))
# g2.close()
# print(inspect.getgeneratorstate(g2))



'''
生成器，
'''
#子生成器
def average_gen():
    pass
    total =0
    average = 0
    count = 0
    while True:
        new_num = yield average     # next 碰到 yield 就停止
        count +=1
        total +=new_num
        average = total / count

#委托生成器
def proxy_gen():
    while True:
        yield from average_gen()

def main():
    cacl_average = proxy_gen()
    next(cacl_average)      #预激活生成器
    print(cacl_average.send(10))    #打印10.0
    print(cacl_average.send(20))
    print(cacl_average.send(30))


#调用方
# if __name__ == '__main__':    #如果函数的 名字 等于 main 就执行 main()函数
#     main()
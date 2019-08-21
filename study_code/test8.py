'''
协程
'''

# def simple_coroutine():
#     print('-> coroutine started')
#     x = yield  # 该协程只需从调用方那里接收数据，所以yield关键字右边没有表达式，默认产出None
#     print('-> coroutine received: ', x)
# p = simple_coroutine()
# next(p)
# p.send(18)  #运行结束 抛出   StopIteration 异常


# def simple_coro2(a):  # 产出两个值的协程
#     print('--> Started: a =', a)
#     b = yield a
#     print('--> Received: b =', b)
#     c = yield a + b
#     print('--> Received: c =', c)
#
#
# p = simple_coro2(14)
# next(p)  #next(p) 预激simple_coro2(a) 函数 代码暂停在 第12行 b = yield a
# # print(next(p))
# # print(p.send(28))
# p.send(28)  # yield a 整体表达式等于 28
# p.send(100)  # yield a+b 整体表达式等于 100


class DemoException(Exception):
    """An exception type for the demonstration."""

def demo_finally():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:  # 特别处理 DemoException 异常
                print('*** DemoException handled. Continuing...')
            else:  # 如果没有异常，那么显示接收到的值
                print('-> coroutine received: {!r}'.format(x))
    finally:  # 不管协程如何结束都想做些清理工作
        print('-> coroutine ending')

my_exc = demo_finally()
next(my_exc)
# my_exc.throw(DemoException)   # .throw 向协程抛出一个异常
my_exc.send(10)
my_exc.send(20)

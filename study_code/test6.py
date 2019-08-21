'''
如果多个线程同时对同一个全局变量操作，会出现资源竞争问题，从而数据结果会不正确
'''
# import threading
# import time
#
# g_num = 0
#
# def work1(num):
#     global g_num
#     for i in range(num):
#         g_num += 1
#     print("----in work1, g_num is %d---"%g_num)
#
#
# def work2(num):
#     global g_num
#     for i in range(num):
#         g_num += 1
#     print("----in work2, g_num is %d---"%g_num)
#
#
# print("---线程创建之前g_num is %d---"%g_num)
#
# t1 = threading.Thread(target=work1, args=(1000000,))
# t1.start()
#
# t2 = threading.Thread(target=work2, args=(1000000,))
# t2.start()
#
# while len(threading.enumerate()) != 1:
#     time.sleep(1)
#
# print("2个线程对同一个全局变量操作之后的最终结果是:%s" % g_num)



'''
加入互斥锁后，其结果与预期相符
'''
# import threading
# import time
#
# g_num = 0
#
# def test1(num):
#     global g_num
#     for i in range(num):
#         mutex.acquire()  # 上锁
#         g_num += 1
#         mutex.release()  # 解锁
#
#     print("---test1---g_num=%d"%g_num)
#
# def test2(num):
#     global g_num
#     for i in range(num):
#         mutex.acquire()  # 上锁
#         g_num += 1
#         mutex.release()  # 解锁
#
#     print("---test2---g_num=%d"%g_num)
#
# # 创建一个互斥锁
# # 默认是未上锁的状态
# mutex = threading.Lock()
#
# # 创建2个线程，让他们各自对g_num加1000000次
# p1 = threading.Thread(target=test1, args=(1000000,))
# p1.start()
#
# p2 = threading.Thread(target=test2, args=(1000000,))
# p2.start()
#
# # 等待计算完成
# while len(threading.enumerate()) != 1:
#     time.sleep(1)
#
# print("2个线程对同一个全局变量操作之后的最终结果是:%s" % g_num)


import random
import threading
import time
import queue

q = queue.Queue(maxsize=10) #queue 消息队列


def producer(name):  # 生产者
    count = 1
    while True:
        q.put("骨头%s" % count)
        print("生产了骨头", count)
        count += 1
        time.sleep(random.randrange(3))


def consumer(name):  # 消费者
    while True:
        print("[%s]取到[%s]并且吃了它..." % (name, q.get()))
        time.sleep(random.randrange(5))

# 两个消费者，1个生产者
p = threading.Thread(target=producer, args=("Tim",))
c1 = threading.Thread(target=consumer, args=("King",))
c2 = threading.Thread(target=consumer, args=("Wang",))

p.start()
c1.start()
c2.start()
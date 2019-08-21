# import multiprocessing
# import time
# def run(name):
#     time.sleep(10)
#     print(name, " 进程启动")
#
# if __name__ == '__main__':
#     mp = multiprocessing.Process(target=run, args=("LJ",))
#     mp.start()
#     mp.join() # 等待进程执行完毕

# import multiprocessing
# import time
# import threading
#
#
# def thread_run():
#     print(threading.get_ident())
#
#
# def run(name):
#     time.sleep(5)
#     print(name, " 进程启动")
#     # 在进程中再启动线程
#     t = threading.Thread(target=thread_run, )
#     t.start()
#
#
# if __name__ == '__main__':  #主进程
#     # 生成多个进程(6个进程)
#     for i in range(6):
#         p = multiprocessing.Process(target=run, args=('hello %s' % i,))
#         p.start()


# from multiprocessing import Process
# import os
# import time
#
# def run_proc():
#     """子进程要执行的代码"""
#     print('子进程运行中，pid=%d...' % os.getpid())  # os.getpid获取当前进程的进程号
#     time.sleep(6)
#     print('子进程将要结束...')
#     print('我的爸爸是，ppid=%d...' % os.getppid())  # os.getppid获取当前进程的主进程号
#
# if __name__ == '__main__':
#     print('父进程pid: %d' % os.getpid())  # os.getpid获取当前进程的进程号 (主进程)
#     p = Process(target=run_proc)
#     p.start()


'''
进程间内存是独立的
'''
import random
from multiprocessing import Process
import os
import time

nums = [11, 22]

def work1():
    """子进程要执行的代码"""
    print("in process1 pid=%d ,nums=%s" % (os.getpid(), nums))
    for i in 'baidu':
        nums.append(i)  #将字符串 baidu 使用append 方法逐次添加到 nums 列表中
        time.sleep(random.random())
        print("in process1 pid=%d ,nums=%s" % (os.getpid(), nums))

def work2():
    """子进程要执行的代码"""
    print("in process2 pid=%d ,nums=%s" % (os.getpid(), nums))
    for i in 'neuedu':
        nums.append(i)  #将字符串 neuedu 使用append 方法逐次添加到 nums 列表中
        time.sleep(random.random())
        print("in process2 pid=%d ,nums=%s" % (os.getpid(), nums))

if __name__ == '__main__':
    p1 = Process(target=work1)
    p1.start()


    p2 = Process(target=work2)
    p2.start()

    p1.join()
    p2.join()
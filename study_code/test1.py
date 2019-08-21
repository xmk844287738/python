'''
装饰器本质
---------------------
版权声明：本文为CSDN博主「曾月天」的原创文章，遵循CC
4.0
by - sa版权协议，转载请附上原文出处链接及本声明。
原文链接：https: // blog.csdn.net / yuetiantian / article / details / 83034087
'''
# import time
#
# def delay(func):    #func => add() 函数
#     def wrapper(*args, **kwargs):   #此处的参数为 add 函数里的参数
#         time.sleep(1)
#         ret = func(*args,**kwargs)  # func => add() 函数, 此处的参数为 add 函数里的参数
#         print("delay 1 second to call %s" % func.__name__)
#         return ret
#
#     return wrapper
#
#
# @delay
# def add(a, b):
#     return a + b
#
#
# if __name__ == "__main__":
#     print(add(3,3))



import time

def display(func):
    def wrapper(*args):
        start_time = time.time()
        count = func(*args)    #此处的 result 变量接收 prime_num 函数的返回值 count(素数的个数)
        end_time = time.time()
        print("the time cost:", str(end_time - start_time))
        return count

    return wrapper

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True

    else:
        for item in range(2, num):
            if num % item == 0:
                return False
        return True

@display
def prime_num(maxnum):  # prime_num => func
    # start_time =time.time()

    count = 0
    for i in range(2, maxnum):
        if is_prime(i):
            print(i)
            count +=1
    return count

    # end_time =time.time()

    # print("the time cost:",str(end_time - start_time))

# prime_num(10000)
result = prime_num(10000)
print("素数个数为：",result)
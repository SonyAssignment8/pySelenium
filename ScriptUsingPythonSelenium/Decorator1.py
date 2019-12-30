import time
import math
def timer(func):
    def inner(a):
        strt=time.time()
        func(a)
        end=time.time()
        print("time taken for execution",end-strt)
    return inner

@timer
def fact_num(n):
    time.sleep(6)
    print(math.factorial(n))
fact_num(6)



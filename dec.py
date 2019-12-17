#using decorater calcuate square and cube of numbers
import time
def timer(func):
    def inner(n):
        start= time.time()
        func(n)
        end=time.time()
        print("time taken for execution",end-start)
    return inner

@timer
def cube(n):
    time.sleep(1)
    for i in range(1,n+1):
        res=i**3
    print(res)

@timer
def square(n):
    time.sleep(1)
    for i in range(1,n+1):
        res=i**2
    print(res)


square(4)
cube(3)
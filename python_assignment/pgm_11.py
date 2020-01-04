# 12 Write a basic program for iterator, decorator and generator
# # generator and iterator pgm
#
#
# add=lambda a,b:a+b
# print(add(4,6))
#
# def sam():
#     print("first")
#     yield
#     print("second")
#     yield
#     print("third")
#     yield
#     print("fourth")
#
# print(sam())
#
# var=sam()
# i=iter(var)
# next(i)
# next(i)
# next(i)
# next(i)
# # next(i)

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
cube(4)

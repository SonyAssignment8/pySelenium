# #decorator example
# import datetime
# from datetime import datetime
# def my_decorator(func):
#     def time():
#         print("something is happening before function call")
#         func()
#         print("something is happening after function call")
#     return time
#
# @my_decorator
# def alaram():
#     print("alarm started")
#
# m=my_decorator(alaram())
#
#
# #decorator program 2
# def my_decorator2(func):
#     def time():
#         if 7<=datetime.now().hour<22:
#             func()
#         else:
#             pass
#
#     return time
#
# @my_decorator2
# def alaram():
#     print("playing alaram music")
#
# d=my_decorator2(alaram())


#generator Program

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#         yield f
#
# for i in fact(4):
#     print(i)

#generator program 2

# def febo(n):
#     a=0
#     b=0
#     c=1
#     for i in range(0,n):
#         a=b
#         b=c
#         c=a+b
#         yield a
# for i in febo(4):
#     print(i,end="")

#generator program 3

# def prime(start,end):
#     for num in range(start,end):
#         if num>1:
#             for i in range(2,num):
#                 if num%i==0:
#                     break
#             else:
#                 yield num
#
# for i in prime(10,20):
#     print(i)


#Example for Iterator

di={"hi","hello","how","are"}
i=iter(di)
for j in range(0,len(di)):
    print(next(i))

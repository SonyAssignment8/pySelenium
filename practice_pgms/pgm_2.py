# from practice_pgms.global_key import *
# def mul():
#     print("multiplication of two number is:",a*b)
# add()

x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"
#
# myfunc()
#
# print("Python is " + x)
def gen():
    for i in range(0,10):
        print(i)
        yield
gen()
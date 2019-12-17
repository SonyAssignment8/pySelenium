#lambda
# x=lambda a,b:a*b
# print(x(10,20))
# def test(n):
#     return lambda a:a-n
# fun=test(2)
# print(fun(10))
#iterator
# l=[10,20,30,40,50]
# a=iter(l)
# for i  in range(0,len(l)):
#     print(next(a))
#custome iterater
# class demo():
#     def __init__(self):
#         self.l = [10, 20, 30, 40, 50]
#         self.index=-1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.index+=1
#         if self.index>=len(self.l):
#             raise StopIteration
#         print(self.l[self.index])
# a=demo()
# a.__iter__()
# for i in range (0,4):
#     a.__next__()

# def square():
#       x=1
#       while True:
#                 yield x*x
#                 x+=1
# for i in square():
#      if i>100:
#          break
#      print(i)

# def srt():
#     n=1
#     while n<=10:
#            x=n*n
#            yield x
#            n+=1
# values=srt()
# for i in values:
#     print(i)
import math


def is_perfect_square(n):
    return (round(n ** 0.5) ** 2 == n)
print(list(filter(is_perfect_square, [3, 4, 8, 16, 21, 58, 144])))

# l=[1,2,3,4,5]
# l=list(filter(lambda n:n*n,l))
# print(l)
a=10
b=20
assert a>b,False
True
# s=[2,3,4,5,6,7]
# i=iter(s)
# print(i)
#



# l=[1,2,3,4,5]
# # for n in l:
# #     n=n*n
# #     print(n)
# l=[1,2,2,4,1,3]
#print(list([n,map(lambda n:n%2==0,l))])


#def outer(func):
#     def inner(a, b):
#         if a <= b:
#             b,a = a,b
#             return func(a, b)
#
#     return inner
#
#
# # @outer
# def div(a, b):
#     print(a,b)
#     print(a / b)

# o = outer(div)
# o(2, 0)

# class iterator():
#     def __init__(self):
#         self.shworoom = ['oudi', 'xy', 'benz', 'maruth', 'aulto']
#         self.index=-1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.index+=1
#         if self.index >= len(self.shworoom):
#             raise StopIteration
#         print(self.shworoom[self.index])
# h = iterator()
# i=iter(shworoom)
# for x in i:
#     print(i)


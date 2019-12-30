# def add(a,b):
#     return a+b
# print(add(1,3))
#
# z=lambda a,b:a+b
# x=z(1,2)
# print(x)
def f1():
    def inner(a,b):
        print('sum',a+b)
        print('avg',(a+b)/2)
        print()
    inner(1,2)
    inner(2,3)
    inner(4,5)

f1()

#lambda program using maps
# def add(n):
#     return n
num=(1,2,3,4)
print(list(map(lambda n:n+n,num)))



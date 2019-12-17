# Nested Function , not method :
def f1():
    def inner(a,b):
        print("Sum :", a+b)
        print('Average', (a+b)/2)
        print()
    inner(1,2)
    inner(10,40)
    inner(20,40)
    inner(100,400)
f1()
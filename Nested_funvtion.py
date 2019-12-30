#nested method
def f1():
    def inner(a,b):
        print("sum:",a+b)
        print("Average",(a+b)/2)
        print()
    inner(1,2)
    inner(12,24)
    inner(24,45)
    inner(123,456)

f1()

# def ip():
#     a=int(input("enter the value"))
#     b=int(input("enter the value"))
#     return a,b
def div(a,b):
    c=a/b
    return c
def manage(func):
    def inner(a,b):
        if a>b:
            a,b=b,a
        return func(a,b)
    return inner

div1=manage(div)
c=div1(1,0)
print(c)






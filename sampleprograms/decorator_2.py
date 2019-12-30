def outer(func):
    def inner(a,b):
        print("the numbers are:",a,b)
        if b == 0:
            a, b = b, a
            print("after swaping",a, b)
        div=func(a,b)
        print("the division  is:")
        print(div)
    return inner(0,2)
@outer
def infinity(a,b):
    div = a / b
    return div


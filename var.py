a,b=10,20
print(a,b)
def sample():
    x,y=1,3
    def inner():
        global a,b
        nonlocal x,y
        print("inside func",a,b)
        a,b=b,a
        x,y=y,x
        print(x,y)
        print(a,b)

    inner()
    print(a,b)

sample()







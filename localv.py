a,b = 10,20
def sample():
    x,y= 10,20
    def inner ():
        global a,b
        nonlocal x,y
        a,b = b,a
        x,y = y,x
        print(x,y)
        print(a,b)
    print(x,y)
    inner()
    print(x,y)
sample()
        # a,b = b,a , we can not do that, it wont change valules of a and b so v have to use global variable



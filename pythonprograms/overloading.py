def add(a, b,c=None,d=None):

    if c==None and d==None:
        return a+b
    elif c!=None and d==None:
        return a+b+c
    else:
        return a+b+c+d
print(add(1, 2,3))
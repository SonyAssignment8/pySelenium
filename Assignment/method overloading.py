class Method():
    def add(a,c,b=None,d=None):
        if b==None and d==None:
            return a+c
        elif b!=None and d==None:
            return a+b+c
        else:
            return a+b+c+d
    print(add(1,2))
    print(add(1,2,3))
    print(add(1,2,3,4))
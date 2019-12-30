# def add(a,b):
#     return a+b
# def add(a,b,c):
#     return a+b+c
# def add(a,b,c,d):
#     return ab+b+c+d
#
# print(add(1,2,3,4))
def add(a,b,c=None,d=None):
    if c==None and d==None:
        return a+b
    elif c!=None and d==None:
        return a+b+c

    else:
        return a+b+c+d
print(add(1,3))


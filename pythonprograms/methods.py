a=10
#no parameter no return type
def m1():
    print(a)
m1()

#with parameter ,no return type

def m2():
    return 20
b=m2()
print(b)

#with parameter with return type
def m3(a):
    print(a)
    return "hi"
s=m3(a)
print(s)

#no parameter with return type
def m4():
    print(a)
    return 10
s1=m4()

#slicing
s="java"
a=s[1:]
print(a)
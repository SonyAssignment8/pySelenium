class A():
    b=20
    def __init__(self):
        self.a=10
        c=30
o=A()
print(o.b)
print(o.a)
#print(A.a)local variable

@classmethod
def A1(cls):
    cls.b1=30
def m1(self):
    b=10

l=[3,2,5,8]
l2=[6,5,9,7]
z=map(lambda n:n%2==0,l)
y=map(lambda n,m:n*m,l,l2)
print(list(y))



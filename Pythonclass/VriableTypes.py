class A():
    a=20
    def __init__(self):
        self.b=30
    def m1(self):
        c=40
        print(a)
@classmethod
def m2(cls):
    print(A())


o=A()
o.m1()
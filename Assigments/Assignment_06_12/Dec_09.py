class A:
    b = 20
    def __init__(self):
        self.a = 10
A.b = 20
O = A()
print(O.b)

@classmethod
def A1(cls):
    cls.b = 30


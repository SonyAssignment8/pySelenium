#Method Overriding
class A():
    a = 10
    def a1(self):
        print("Hi")
class B(A):
    b = 20
    def a1(self):
        print("hello")
O = B()
O.a1()
print(O.a)
print(O.b)
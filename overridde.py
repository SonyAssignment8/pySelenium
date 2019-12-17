class A():
    a=10
    def a1(self):
        print("Hi")
class B(A):
    b=23
    def a1(self):
        print("hello")

o=B()
o.a1()
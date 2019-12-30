class A():
    def __init__(self):  #dunder method or magical method
        self.a=12          #default constructor
        print(self.a)

    def a1(self):
        print("Inside method a1")


o=A()
o.a1()
#constructor concept

class A():
    a=12
    def __init__(self):
        print(self.a)

    def a1(self):
        print("inside method ")

o=A()
o.a1()
print(o)
o1=A()
print(o1)

#How to initialse inside constructor

class Human():
    def __init__(self,name,phno):
        self.name=name
        self.phno=phno
    def details(self):
        print("details::","phone number is==>",self.phno,"name is==>",self.name)

h=Human("krishna",123456)
h.details()



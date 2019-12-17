#constructor
class A():
    def __init__(self):
        self.a=12
        print(self.a)
    def a1(self):
        print("inside method")
o=A()
o.a1()

class Human():
    def __init__(self,name,phno):
        self.name=name
        self.phno=phno
    def details(self):
        print("Details are:",self.name)
        print("phone num is:",self.phno)
o=Human("abc","6565646")
o.details()




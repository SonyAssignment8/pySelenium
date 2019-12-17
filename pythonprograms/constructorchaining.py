class Human():
    def __init__(self):
        self.a=10
        self.b=100
        print("Human")
    def m1(self):
        print("hi")
class Emp(Human):
    def __init__(self):
        super().__init__()
        print("Emp")
o=Emp()
o.m1()
#parameterised constructor
class Human():
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def m1(self,a):
        print("hi")
class Emp(Human):
    def __init__(self,name,address):
        super().__init__(name,address)
        print("Emp")
o=Emp('aaa','banglore')
o.m1(10)

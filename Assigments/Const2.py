class Parent():
    a = 10
    def pclass(self):
        self.a = 10
        print('Parent method')
    def __init__(self):
        print("inside parent class constructor")

class Child(Parent):
    b = 10
    def cClass(self):
        self.b=10
        print('child method')
    def __init__(self):
        Parent.__init__(self)
        print("inside child class constructor")
Obj = Child()
Obj.a
Obj.b
Obj.pclass()
Obj.cClass()
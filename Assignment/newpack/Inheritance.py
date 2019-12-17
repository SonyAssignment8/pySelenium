class Inheritance():
    a=10
    def __init__(self):
         self.b=20
    def m1(self):
        print('m1 method running from super class')

class SingleInheritance(Inheritance):
    a=20
    def __init__(self):
        super(). __init__()
        #Inheritance. __init__(self)
    def  m1(self):
         print('m1 method running from sub class')
o=SingleInheritance()
print(o.a)
o.m1()
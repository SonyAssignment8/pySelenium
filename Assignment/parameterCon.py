class Human1():
    def __init__(self,name,address):
        self.a = 10
        self.b = 100
        print('Class Human')

    def m1(self,a):
        print('hi')


class Emp(Human1):
    def __init__(self,name,address):
        Human1.__init__(self,name,address)
        super().__init__(name,address)
        print('inclass emp')


o = Emp('AAA','Bangalore')
o.m1(1)


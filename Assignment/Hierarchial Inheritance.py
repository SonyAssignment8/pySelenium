class Animal():
    def v1(self):
        print('Animals')
class Lion(Animal):
    def v2(self):
        print("Lion")
class Tiger(Animal):
    def v3(self):
        print('Tiger')
o1=Lion()
o1.v1()
o1.v2()
o2=Tiger()
o2.v1()
o2.v3()

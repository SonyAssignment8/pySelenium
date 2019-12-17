#single level inheritance
class Animal():
    a="Animal"
    def animal(self):
        print("animal")
class Dog(Animal):
    b='Dog'
    def dog(self):
        print("animal is dog")
d=Dog()
print(d.b)
print(d.a)
d.animal()

#multilevel inheritance
class Puppy(Dog):
    def puppy1(self):
        print("puppy")
p=Puppy()
p.dog()
p.animal()

#hierarchical inheritance
class Vehicle():
    def v1(self):
        print("Vehicles")
class Two_Wheeler(Vehicle):
    def v2(self):
        print("Two wheeler is a vehicle")
class Three_Wheeler(Vehicle):
    def v3(self):
        print("Three wheeler is a vehicle")
v=Two_Wheeler()
v.v1()
v.v2()
v3=Three_Wheeler()
v3.v1()
v3.v3()

#multiple inheritance
class c1():
    def client1(self):
        print("client1")
class c2():
    def client2(self):
        print("client2")
class company(c1,c2):
    def company(self):
        print("company have client 1 and 2")
c=company()
c.client1()
c.client2()

#hybrid inheritance
class c1():
    def client1(self):
        print("client1")
class c2(c1):
    def client2(self):
        print("client2")
class c3(c1):
    def client3(self):
        print("client3")
class c4(c2,c3):
    def client4(self):
        print("client4")
c=c4()
c.client1()
c.client2()
c.client3()
c.client4()

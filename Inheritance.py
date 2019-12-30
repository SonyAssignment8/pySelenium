#single & multilevel
class Animal():
    a=1
    def animal1(self):
        print("inside method-->animal")
class Dog(Animal):
    b=1
    def dog1(self):
        print("inisde method-->DOG")

class Puppy(Dog):
    def puppy1(self):
        print("inside method--->puppy")

o =Puppy()
print(o.a)
print(o.b)
o.animal1()
o.dog1()
o.puppy1()
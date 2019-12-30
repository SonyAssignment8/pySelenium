#inheritance concept
class animal():
    a=1
    def animal1(self):
        print("inside method --->animal")
        o.dog1()

class Dog(animal):
    b=1
    def dog1(self):
        print("inside method -->DOG")

o=Dog()
print(o.a)
print(o.b)
o.animal1()


class Animal () :
    a=1
    def animal(self):
        print("Inside Method---->animal")

class Dog (Animal) :
    b=1
    def dog1(self) :
        print("Inside Method---> DOG")
class puppy (Dog)  :
    def puppy1(self):
        print(" inside method----> pupy")

o=puppy
print(o.a)
print(o.b)
o.animal()
o.puppy()




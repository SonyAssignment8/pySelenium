class Animal () :
    a=1
    def animal(self):
        print("Inside method-->Animal")   # print statement


class Dog (Animal):                       # Inherite Animal class
    b=2
    def dog1(self):
        print("Inside Method---> DOG")    # print statement
o=Dog()
print(o.a)
print(o.b)
o.animal()



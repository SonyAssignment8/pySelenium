class Animal():
    a = 10

    def type(self):
        print('inside method-----type')


# Single inheritance
class Dog(Animal):
    b = 1

    def breed(self):
        print('inside method---type')


o = Dog()
print(o.a)
print(o.b)
o.type()
o.breed()


# multiple inheritance
class puppy(Dog):
    def puppy1(self):
        print('inside method----> puppy')


o = puppy()
print(o.a)
print(o.b)

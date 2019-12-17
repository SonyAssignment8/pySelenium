class Animal():
    def speak(self):
        print("Animal Speaking")


# child class Dog inherits the base class Animal
class Dog(Animal):
    def bark(self):
        print("dog barking")


# child class puppy inherits the base class Animal
class Puppy(Dog):
    def bark1(self):
        print("puppy barking")

P = Puppy()
P.bark1()
P.bark()
P.speak()

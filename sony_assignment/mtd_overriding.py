class Animal:
    def eating(self):
        print("eating")

    def sleeping(self):
        print("sleeping")
class Dog(Animal):
    def eating(self):
        print("dog is eating")
    def running(self):
        print("dog is running")
a=Animal()
a.eating()
a.sleeping()
d=Dog()
d.eating()
d.sleeping()
d.running()
class Human():
    def behave(self):
        print("at home")
    def behave(self,a=None):
        print('At office')
class Person(Human):
    def behave(self):
        print("i behave different at home")
p=Person()
p.behave()

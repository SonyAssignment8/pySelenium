# By Composition ---Has a Relationship
class Car():
    brand = "Audi"
    Color = "White"
    def info(self):
        print("The brand of CAR :", self.brand)
        print("The color of car :" , self.Color)
class Engine():
    Car().info()
    def engineninfo(self):
       print("This is a method in engine")

o = Engine()
o.engineninfo()





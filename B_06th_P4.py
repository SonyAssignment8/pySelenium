#BY Composition ---->HAS _A Relationship
class Car():
    brand = "audi"
    color = "white"

    def info(self):
        print("The brand of car:",self.brand)
        print("The color of car:",self.color)
class Engine():
    o = Car()
    o.info()
    def Engineinfo(self):
        print("this is a method in engine")
o = Engine()
o.Engineinfo()
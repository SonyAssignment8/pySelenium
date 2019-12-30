# By Composition or Has A RelationShip nothing but creating one class object in another class
class car():
    brand="xyz"
    engin="4-stroke engine"
    colour="Red"
    milage="23/Ltr"
    wheel="mekwheel"
    def feedback(self):
        print("less cost high performance")
    def resale(self):
        print("Resale value is high")

class CarInf():
    c=car()
    c.resale()
    c.feedback()
    def m1(self):
        print("Carinfo running")
ci=CarInf()
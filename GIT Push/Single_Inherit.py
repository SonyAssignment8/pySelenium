class Vehicle():
    model = 2019
    def speed(self):
        print("Display speed")
class Motorcycle(Vehicle):
    cc = 160
    def rtr(self):
        print("race - throttle - response")
V = Motorcycle()
V.speed()
V.rtr()
print(V.cc)
print(V.model)
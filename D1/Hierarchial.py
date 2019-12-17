class Vehicle():
    def v1(self):
        print("vehicles")
class Two_wheeler(Vehicle):
    def v2(self):
        print("Two wheeler is a vehicle")
class Three_wheeler(Vehicle):
    def v3(self):
        print("three wheeler is vehicle")
v = Two_wheeler()
v.v1()
v.v2()

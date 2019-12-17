class Vehicle():
    def v1(self):
        print('vehicles')
class Two_Wheeler(Vehicle):
    def Tw2(self):
        print("two wheeler is a vehicle")
class Three_Wheeler(Vehicle):
    def TW3(self):
        print("two wheeler is a vehicle")
o = Two_Wheeler()
o.Tw2()
o.v1()
o1 = Three_Wheeler()
o1.TW3()
o1.v1()

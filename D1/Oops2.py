class Vehicle():
    tyrePressure = 35
    Acceleration = 60

    def Speed(self):
        print("Vehicle is travelling at",self.Acceleration,"Kms")
    def destination(self):
        print("Highway on my Pomp")
v = Vehicle()
print("Tyre Pressure is:",v.tyrePressure)
v.destination()
v.Speed()
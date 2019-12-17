class Car():
    brand='i20'
    color='black'
    regno='ka3h102'
    cost=500000
    def speed(self):
        print("car is moving with the speed 120/km")
    def service(self):
        print("the car is in good condition ")

class vuhicle():
    c=Car()
    c.service()
    c.speed()
    print("the car informations are brand={0},color={1}".format("i20","black"))
v=vuhicle()

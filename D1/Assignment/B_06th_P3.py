class Car():
    make = 2019
    type = "petrol"
    cc = 1500
    brand = "volkswagen"

    def speed(self):
        print("The car can do 180km/hr")
    def mileage(self):
        print("The mileage of the car is 18kmpl")
    def info(self):
        print("make:{0},type:{1},cc:{2},brand:{3}".format(self.make,self.type,self.cc,self.brand))

obj = Car()
obj.speed()
#print(obj.brand)
obj.info()


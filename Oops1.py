#Self keyword holds the address of the current object which is under execution : Eg This keyword in java
class Human():
    height=6
    weight = 70
    colour = "Brown"
    print("Inside the class Colour-->",colour)
    def sleeping(self):
        print("Am Sleeping")
        print("inside the method-->",self.colour)
    def eating(self):
        print("Am belting")

O = Human()
print(O.height)
O.sleeping()
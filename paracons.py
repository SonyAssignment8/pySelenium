class Human():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        print("To class human")
    def M1(self,a):
        print(a)
        print("HI")

class Emp(Human):
    def __init__(self, name, address):
        Human.__init__(self, name, address)
        print(self.name)
        print(self.address)
        print("in a class")
o=Emp('raj', 'banglore')
o.M1(10)


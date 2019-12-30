class Human():
    def __init__(self, name, city):
        self.a = 10
        self.b = 100
        print("To class human")
    def M1(self):
        print("HI")

class Emp(Human):
    def __init__(self, name, city):
        Human.__init__(self, name, city)
print("in a class")
o=Emp('atul','jbp')
o.M1()


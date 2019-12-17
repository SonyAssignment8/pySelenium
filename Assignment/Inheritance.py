class Stationaryshop():
    pen=10
    pencil=20
    def Stationary(self):
        print('School method is executed')
#Single Inheritance
class School(Stationaryshop):
    def Schoolitems(self):
        print('Items needed in school')
#Multilevel Inheritance
class College(School):
    def Collegeitems(self):
        print('Items needed for College')
o=College()
print(o.pen)
print(o.pencil)
o.Collegeitems()

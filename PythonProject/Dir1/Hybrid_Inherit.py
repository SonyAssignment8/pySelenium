class Laptop():
    def Lenevo(self):
        print('Lenevo laptop')
class TV(Laptop):
    def Oneplus(self):
        print('Hi....one plus TV')
class Moblie(TV):
    def oneplus(self):
        print('Never settle')
class Both(TV,Moblie):
     def MI(self):
        print('Both TV and mobiles')
O = Both()
O.Lenevo()
O.Oneplus()
O.oneplus()
O.MI()
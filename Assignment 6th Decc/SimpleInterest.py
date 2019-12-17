#Claculate the simple interest
class SimpleInterest():
    p=int(input('Enter the value of p'))
    n=int(input('Enter the value of n'))
    r=int(input('Enter the value of r'))
    simple=0
    def SI(self):
        simple= (self.p*self.n*self.r)/100
        print('The simple interest of  the given values is:',simple)
s=SimpleInterest()
s.SI()
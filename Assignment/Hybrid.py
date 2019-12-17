#Hybrid Inheritance
class Festival():
    def client1(self):
        print('Festival')
class Clothes(Festival):
    def client2(self):
        print('New Clothes')
class Snacks(Festival):
    def client3(self):
        print('Snacks')
class Diwali(Clothes,Snacks):
    def client4(self):
        print('Diwali')
o=Diwali()
o.client1()
o.client4()
o.client2()
o.client3()


class Human():
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone

    def details(self):
        print('Details:',self.name)
        print('Phone number:',self.phone)
o=Human('Divya','912843490904')
o.details()
#constructor chaining
class animal(Human):
    def __init__(self,name):
        Human.__init(self,name)
        super().__init__(name)
    def a1(self):
        print('hi')
a=animal('lion')
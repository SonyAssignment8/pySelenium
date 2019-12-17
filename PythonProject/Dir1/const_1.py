class Human():
    # Non-parameterized constructor
    def __init__(self):
        a = 10
        b = 100
        print("inside constructor human")

    # Parameterized constructor
    def __init__(self, name, address):
        self.name = name
        self.address = address
        print("inside Parameterized constructor Human")
    def m1(self):
        print('hi')

class Emp(Human):
    # Non-parameterized constructor
    def __init__(self):
        Human.__init__(self)
        super().__init__()
        print("inside constructor Emp")

    # Parameterized constructor
    def __init__(self, name, address):
        Human.__init__(self, name,address)
        super().__init__(name, address)
        print("inside Parameterized constructor Emp")

o = Emp('hjio', 'hlkjli')
o.m1()
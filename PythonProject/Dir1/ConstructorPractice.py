class A():
    def __init__(self):
        self.a = 12
        print(self.a)

    def a1(self):
        print('inside method a1')

    def __init__(self, name, phno):
        self.name = name
        self.phno = phno
    def details(self):
        print('details:', self.name)
        print('phone:', self.phno)
O = A()
O.a1()
O = A("jyoti","12344")
O.details()


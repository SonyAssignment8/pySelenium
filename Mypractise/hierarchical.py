class Parents():
    def funct1(self):
        print("This is function 1")

class Parent1(Parents):
    def funct3(self):
        print("This is function 3")

class child(Parents):
    def funct2(self):
        print("This is function 2")

a = child()
a.funct1()
a.funct2()



#multi level in heritane
class Two_wheeler():
    def bike(self):
        print("Bike")
class Three_Wheeler(Two_wheeler):
    def auto(self):
        print("auto")

class Four_wheeler(Two_wheeler):
    def car(self):
        print("car")
th=Three_Wheeler()
th.bike()
th.auto()
th1=Four_wheeler()
th1.bike()
th1.car()


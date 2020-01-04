# 10 Write a Program for encapsulation?
class RBI:

    def __init__(self):
        self.__updateSoftware()

    def sbi(self):
        print('sbi bank')

    def hdfc(self):
        print("hdfc bank")

    def __updateSoftware(self):
        print('updating software')

b= RBI()
b.sbi()
b.hdfc()

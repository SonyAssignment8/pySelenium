#constructor concept on day-5
class Human():
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr

    def m1(self,a):
        print("hi")

class Emp():
    def __init__(self,name,addr):
        Human.__init__(self,name,addr)

o=Emp("kk",12)






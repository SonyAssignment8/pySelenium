class Human():
    def __init__(self,name,phno):
        self.name = name
        self.phno = phno
    def details(self):
        print("details:",self.name)
        print("Phno:",self.phno)
o = Human("anu","1234567990")
o.details()
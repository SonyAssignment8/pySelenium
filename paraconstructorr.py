class Human():
    def __init__(self,name,phno):
        self.name = name
        self.phno = phno

    def details(self):
        print("details :", self.name)
        print("phno", self.phno)


o=Human("Atul","123456766")
o.details()
class Vehicle():
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "car details are like this." %(self.name ,self.kind,self.value)
        return desc_str
print(car1.desccription())
print(car2.description())
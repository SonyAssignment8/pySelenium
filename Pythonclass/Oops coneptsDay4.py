class Human():
    height=6
    weight=50
    def walking(self):
        print("walking.....")
        print("inside method",self.weight)
    def sleeping(self):
        print("sleeping....")
        print("inside meyhod using class name",Human.weight)
o=Human()
print("height of human",o.height)
o.walking()
o.sleeping()
print("weight of human",o.weight)
print("address of object",o)



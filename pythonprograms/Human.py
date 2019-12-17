class Human():
    height=6
    weight=50
    color='white'
    def walking(self):
        print("the height is:",self.height)
        print("walking.....")
    def sleeping(self):
        print("sleeping......")
    def climbing(self):
        print("hi")
o=Human()
print(o.color)
o.sleeping()
o.walking()
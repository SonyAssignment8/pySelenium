class Projector():
    name="Epson"
    colour="white"
    def Display(self):
        print("used to display ")
    def playvideos(self):
        print("can watch movie in big screen")

p=Projector()
print(p.colour)
print(p.name)
p.Display()
p.playvideos()

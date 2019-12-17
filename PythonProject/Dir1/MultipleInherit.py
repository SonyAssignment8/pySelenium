class Geometry():
    sides = int(input("Number of sides:"))
    def draw(self):
        print("drawing a pattern ")
class Sides():
    def numOfSides(self):
        print("It contains sides:", self.sides)
class Sqaure(Geometry, Sides):
    def drawSqaure(self):
        print("sqaure pattern")
S = Sqaure()
S.draw()
S.numOfSides()
S.drawSqaure()
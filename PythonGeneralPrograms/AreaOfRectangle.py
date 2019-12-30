#Area of rectangle

class Rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def getarea(self):
        print("Area of the rectangle is==>",self.length*self.breadth)

class Square(Rectangle):
    def __init__(self,side):
        super(Square, self).__init__()
        self.side=side
    def getarea(self):
        print("Area of square is==>",self.side*side)

sq=Square(2)
sq.getarea(2)
sq.getarea(2,2)




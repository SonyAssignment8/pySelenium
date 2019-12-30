class Rectangle():
    # length=None
    # breadth=None

    def __init__(self,length,breadth):
        Rectangle.length=length
        Rectangle.breadth=breadth

    def getarea(self,length,breadth):
        print("Area of the rectangle",self.length,self.breadth)
class Square(Rectangle):
    def __init__(self,side):
        Square.side=side
    def getarea(self,side):
        print("Area of Square is:==>",side*side)

rq=Square()
rq.getarea(2)
rq.getarea(2,4)



























# class Rectangle():
# 	def __init__(self,length,breadth):
# 		self.length = length
# 		self.breadth = breadth
# 	def getArea(self):
# 		print(self.length*self.breadth," is area of rectangle")
# class Square(Rectangle):
# 	def __init__(self,side):
# 		self.side = side
# 		Rectangle.__init__(self,side,side)
# 	def getArea(self):
# 		print(self.side*self.side," is area of square")
# s = Square(4)
# r = Rectangle(2,4)
# s.getArea()
# r.getArea()
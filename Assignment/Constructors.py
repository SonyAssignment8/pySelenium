class Human():
      def __init__(self):
          self.a=10
          self.b=100
          print('Class Human')
      def m1(self):
          print('hi')
class Emp(Human):
    def __init__(self):
        Human. __init__(self)
        super(). __init__()
        print('inclass emp')
o=Emp()
o.m1()


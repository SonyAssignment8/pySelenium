# By composition or HAS A relationship
class Car():
    name = 'santro'
    brand = "Hyundai"
    colour='berry red'
    model_year = 2009
    def displayDetails(self):

       print("The name:{0} is a car of brand:{1} with colour:{2} and make year model_year:{3}".format(self.name,self.brand,self.colour,self.model_year))

class Engine():
    def engine_info(self):
        print("this is a method in engine")
Car().displayDetails()
''' this object should be created so that any changes is done to Engine class
it will be reflected to the class'''
o = Engine()
o.engine_info()


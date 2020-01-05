class car():
    def __init__(self,model,colour):
        self.__model = model
        self.colour =colour
    def making(self):
        print("the car color is " + self.colour)
        print("the car model is ",self.__model)

    def __service(self):
        print("service is good")

#provide getter and setters
    def getmodel(self):
        return self.__model

    def setmodel(self,model):
        self.__model=model

    def getservice(self):
        return self.__service()
c=car(123,'red')
c.making()
c.getservice()
c.setmodel(456)
c.making()
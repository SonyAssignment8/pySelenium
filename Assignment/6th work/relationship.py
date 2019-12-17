#By Composition or HAS-A Relationship
class car():
    colour='red'
    speed=120
    brand='tata'
    name='maruthi 800'
    def performance(self):
        print('The details if the car are:','\n',self.colour,'\n',self.speed,'\n',self.brand,'\n',self.name)
        #print('colour={0},speed={1},brand={2},name={3}'.format(self.colour,'\n',self.speed,'\n',self.brand,'\n',self.name))
class Engine():
    def service(self):
        print('service is done')
    c=car()
    c.performance()
e=Engine()
e.service()

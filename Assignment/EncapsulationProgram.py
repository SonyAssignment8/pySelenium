# #example 1 for encapsulation
# class Fan:
#     def __init__(self):
#         self.__remote()
#     def drive(self):
#         print("fan is on")
#     def __remote(self):
#         btn=int(input("press one to switch on fan and 0 to switch off the fan"))
#         if btn==1:
#             print("fan is on")
#         else:
#             print("fan is off")
# f=Fan()
# f.__remote() #we can not call it outside the class because it is a private method

#example 2 for encapsulation in python
class Car():
    __maxspeed=0
    __name=" "
    def __init__(self):
        self.__maxspeed=200
        self.__name="benz car"
    def drive(self):
        print("driving")
        print(self.__maxspeed)
    def setspeed(self,speed,carname):
        self.__maxspeed=speed
        self.__name=carname
        print(self.__maxspeed)
c=Car()
c.drive()





class A():
    def m1(self):
        pass


from abc import *


class Vehicle():
    @abstractmethod
    def no_of_wheels(self):
        pass
name1 = 'jyoti'
name2 = 'dhanendra'
name3 = 'sahu'
print("name1={0},name2={1},name3={2}".format(name1,name2,name3))

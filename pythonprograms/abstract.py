#abstract class
class A():
    pass
#abstract method
def m1():
    pass

from abc import *
class vehical():
    @abstractmethod
    def no_of_wheels(self):
        pass
v=vehical()
v.no_of_wheels()

#string formatting
name1='tyss1'
name2='tyss2'
print('name1={0},name2={1}'.format(name1,name2))

#filehandling
f=open("abc.txt","a")
f.write("\nhello")
f.close()

f1=open("abc.txt","r")
data=f1.read()
print(data)
f1.close()

class Recurssion():
    print('Print numbers from 1 to 100')
    def m1(self,i):
          if i<=100:
           print(i)
           i+=1
           self.m1(i)
a=Recurssion()
a.m1(1)
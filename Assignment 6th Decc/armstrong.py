#Check if the given number is armstrong number or not
n=1634
p=0
temp=n
sum=0
while(n>0):
    p=p+1
    n=n//10
n=temp
from math import pow
while(n>0):
    r=n%10
    sum=sum+pow(r,p)
    n=n//10
if temp==sum:
    print('The given number is armstrong')
else:
    print('The given number is not armstrong')
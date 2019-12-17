#Check if the given number is strong or not
from math import factorial
n=145
sum=0
r=0
temp=n
while(n>0):
    r=n%10
    sum=sum+factorial(r)
    n=n//10
if temp==sum:
    print('The given number is strong')
else:
    print('The given number is not strong')

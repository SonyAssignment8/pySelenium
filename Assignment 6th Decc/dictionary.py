#WAP to generate dictionary that contains no from 1 to n in the form of x,x*x,x*x*x
from math import pow
x=int(input('Enter the key'))
d={(x):'AAA',pow((x),2):'BBB',pow((x),3):'DDD',pow((x),4):'CCC'}
print(d)

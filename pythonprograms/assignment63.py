#calculate simple interesr
principle=int(input("enter principle amount:"))
time=int(input("enter time in years:"))
rate=int(input("enter rate:"))
si=(principle*time*rate)//100
print("simple interest is:",si)

#arm strong number r not
num=int(input("enter the number:"))
sum=0
temp=num
while num>0:
    digit=num%10
    sum+=digit**3
    num//=10
if temp==sum:
    print("its armstrong:")
else:
    print("its not armstrong:")

#strong number==sum of fact of its digit
sum1=0
num=int(input("Enter a number:"))
temp=num
while(num):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i=i+1
    sum1=sum1+f
    num=num//10
if(sum1==temp):
    print("The number is a strong number")
else:
    print("The number is not a strong number")

#generate random number and append in list
import random
num1=int(input("enter starting range:"))
num2=int(input("enter ending range:"))
print(random.randrange(num1,num2))

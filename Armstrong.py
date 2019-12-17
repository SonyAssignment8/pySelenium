
num=int(input("check Armstrong number"))

sum=0
temp=num
p=int(input("enter power number"))
while num>0:
    d=num%10
    sum=sum+d**p
    num//=10
if sum==temp:
    print("Armstrong")
else:
    print("Not Armstrong")
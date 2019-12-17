num=int(input("Enter Strong number"))
temp=num
sum=0
while num>0:
    f=1
    r = num % 10
    for i in range(1,r+1):
        f=f*i
    num = num // 10
    sum=sum+f

print(sum)
if sum==temp:
    print("Strong")
else:
    print("Not Strong")
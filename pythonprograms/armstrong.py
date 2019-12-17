num=153
temp=num
po=0
while num>0:
    num=num//10
    po+=1
armnum=0
num=temp
while num>0:
    rem=num%10
    num=num//10
    armnum=armnum + pow(rem,po)
print(armnum)
if temp==armnum:
    print("number is armstrong")
else:
    print("number is not armstrong")
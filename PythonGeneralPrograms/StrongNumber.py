#find given number is strong or not
num=145
temp=num
strong = 0
while num>0:
    fact=1
    rem=num%10
    for i in range(1,rem+1):
        fact=fact*i
    strong=strong+fact
    num = num // 10
if temp==strong:
    print("number is strong")
else:
    print("number is not strong")


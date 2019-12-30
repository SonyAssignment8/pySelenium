# z=lambda n:print("greater than 0") if n>0 else print("its less than 0")
# z(-1)
# print([i for i in range(0,6) if i>2])
n=153
temp=n
count=0
while(n>0):
 n=n//10
 count+=1
 print(count)
 asum = 0
 while(temp>0):
    rem=temp%10
    asum=asum+pow(count,rem)
    n = n // 10
    print(asum)

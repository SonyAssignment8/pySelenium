#count the number of digits in the given number
s=1234
count=0
r=0
sum=0
while(s>0):
    r=s%10
    sum=sum*10+r
    count=count+1
    s= s//10
print(count)


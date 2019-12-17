#Average of numbers
l=[10,20,30,40,50,60,70,80]
sum=0
avg=0
for i in range(0,len(l)):
    sum=sum+l[i]
    avg=sum/len(l)
print(avg)
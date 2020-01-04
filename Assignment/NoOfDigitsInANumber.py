#36. Write a code to count digits from a given number.
num=145241
count=0
while num>0:
    rem=num%10
    num=num//10
    count +=1
print(count)
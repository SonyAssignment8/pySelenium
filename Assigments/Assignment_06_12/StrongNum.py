import math
num = int(input("Enter a number to check strong number:"))
temp = num
sum1, rem = 0, 0
while num > 0:
    rem = num % 10
    sum1 = sum1 + math.factorial(rem)
    num = num//10
if temp == sum1:
    print('Given number', temp, 'is a Strong Number')
else:
    print('Given number', temp, 'is not a Strong Number')

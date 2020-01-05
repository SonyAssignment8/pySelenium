# 3.Write a program to print Fibonacci series
n = int(input("Enter maximum range:"))
previousNumber = 0
nextNumber = 1
sum = 0
if n in (0,1):
    print(previousNumber)
elif n==2:
    print(previousNumber,end=' ')
    print(nextNumber)
else:
    for i in range(0,n,1):
        print(previousNumber,end=' ')
        sum = previousNumber + nextNumber
        previousNumber = nextNumber
        nextNumber = sum


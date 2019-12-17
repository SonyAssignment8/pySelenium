#9.WAP to count no of the digits in a given number
n = int(input("Enter the number:"))
count = 0
while(n>0):
    n  = n // 10
    count = count + 1
    print("No of digits in",n,"is",count)

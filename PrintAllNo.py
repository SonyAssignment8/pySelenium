# WAP to Print all numbers in a range divisible by  a given numbers

lower= int(input("Enter lower range: "))
upper= int(input("Enter upper range: "))
div=   int(input("Enter Divided by: "))
for i in range (lower, upper+1):
    if(i%div==0):
        print(i)


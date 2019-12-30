# WAP to Print all numbers in a range divisible by a given numbers :

lower=int(input("Enter lower range limit:"))       # lower Range given by user
upper=int(input("Enter upper range limit:"))       # Upper Limit is given by user
n=int(input("Enter the number to be divided by:"))
for i in range(lower,upper+1):
    if(i%n==0):
        print(i)
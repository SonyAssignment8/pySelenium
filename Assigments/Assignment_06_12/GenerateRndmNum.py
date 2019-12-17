# Ques-15: Generating random number according to user's input
import random

a = int(input("Enter lower limit for range:"))
b = int(input("Enter higher limit for range:"))
n = int(input("Enter how many random numbers to be generated:"))
l = []
for i in range(0, n):
    r = random.randint(a, b)
    l.append(r)
print("Generated list from random numbers is:", l)

# Ques-32 Generating 10 random number
for i in range(0,10):
    print(random.randint(60,90))

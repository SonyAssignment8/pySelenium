#List comprehension
#To print random odd numbers
import random
print([i for i in range(random.randint(5,25)) if i%2==1])

#prime number
n=5
print([i for i in range(1,11) if n%i==0])


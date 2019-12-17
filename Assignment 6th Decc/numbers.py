#generate random numbers the range and append them to a list
import random
l=[]
num=int(input('Enter the number of elements to be added in the list'))
for i in range(num):
     element=random.randint(1, 50)
     l.append(element)
print(l)
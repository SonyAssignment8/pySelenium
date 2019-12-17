#check if the given number is perfect square
import math
def perfect_square(n):
    sr=math.sqrt(n)
    return (sr-math.floor(sr)==0)
#using filters
print(list(filter(perfect_square,range(0,26))))

#convert list of string to upper case

print(list(map(lambda i :i.upper(),['apple','mango','grapes','dates'])))

#filter special character from the given string
print(list(filter(lambda i:i>='A' and i<='Z' or i>='a' and i<='z','sad21567@#$#%')))
print(list(map(lambda i:i>='A' and i<='Z' or i>='a' and i<='z',['sad21567@#$#%'])))

#filter the duplicate values
print(set(filter(lambda i:i,[10,10,20,30,40,30])))

#select even items from drop down
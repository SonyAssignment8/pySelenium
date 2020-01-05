#Revrse a string
s="sony assignment"
print(s)
def reverse(s):
    str=""
    for i in s:
        str=i+str
    return str
print("the reversed string is:",reverse(s))


#listcompherhension
print ([ letter for letter in 'Python class' ])

#Fibonocci

def fibonacci(n):
    if n<0:
        print("incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(10))


#Decorator
def outer(func):
    def inner():
        print("hi")
        func()
    return inner
@outer
def wish():
    print("hello")
wish()

#Iterator
str="class","bench","board"
s=iter(str)
print(next(s))

#generator
def PowTwoGen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

#print numbers
print([num for num in range(7)])

#set difference
s1={3,6,12,76,44}
s2={2,6,34,44,65}
print(s1.difference(s2))

#To get all the values in dict
d={'name':"mike",'age':12}
print(d.values())

#To find missing letters
alphabet = "abcdefghijklmnopqrstuvwxyz"
lst=list(alphabet)
def missing_letters(lst1):
    missing = []
    for key in lst:
        if key not in lst1:
            missing.append(key)
    return ''.join(missing) or None
print(list(missing_letters(['r','t','z'])))


#print in alphabetical order

str="d r e a h"
w=str.split()
w.sort()
print("the sorted words")
for word in w:
    print(word)

#Method overriding

class Parent:
    def anything(self):
        print('Function defined in parent class!')

class Child(Parent):
    pass

obj2 = Child()
obj2.anything()

#print key and value in diffrent lines
d={'name':"El",'age':10}
print(d.values())
print(d.keys())

#Replace a string
str="hi hello hi"
s=str.replace("hi","hai")
print(s)

#to replace alternate char with *
msg="hello"
print("*".join("hello"))

#sort a list
lst=[23,12,54,75]
a=lst.sort()
print(a)

#swap 2 numbers
a=20
b=30
a,b=b,a
print("after swaping",(a,b))

#To revome duplicates in list
a=[10,12,14,23,12,22,46,33,12,10]
dup_items=set()
uni_items=[]
for i in a:
    if i not in dup_items:
        uni_items.append(i)
        dup_items.add(i)

print(dup_items)

#code to reverse a string

str="Hello"
string=str(::-1)
print(string)

#even and odd numbers seeperately

num=[2,3,5,6,3,34,22,56,79,7,8,10]
odd=[]
even=[]
if i%2==0:
    even.append(i)
else:
    odd.append(i)

#return len of longest number

num_lst=[123,4232,91238,2442,234,123]
for i in num:


#Read a file and reverse each line
file = open("hello.txt", 'r')
lines = file.readlines()
print(lines)
lines.reverse()
print(lines)
for i in lines:
    print(i[::-1])

#replace a specific word in the file
file = open("hello.txt", 'r')
actual=f.read().replace("xyz","How")
print("after replacing ",actual)


#read a file and count occurance of each word
file = open("hello.txt", 'r')
lines = file.readlines()
print(lines)
print(count(lines))

#store dict vales in a file
d ={1:"hi",2:"hello",3:"how",4:"are",5:"you"}
f=open("TextFile2.txt","w")
f.write(str(d.values()))
print("written successfully...")
f.close()


#custom iterator
class Iterator():
    def __init__(self):
        self.car=["maruthi","suzuki","bmw","benz"]
        self.index=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.index=+1
        if self.index>=len(self.car):
            raise StopIteration
        print(self.car[self.index])

i = Iterator()
for j in i:
    print(j)















# Ques-4: Avg od sum of elements of list
list1 = []
for i in range(0, 5):
    a = int(input("Enter an element for list:"))
    list1.append(a)
print("list given by user is: ", list1)
sum = 0
l = list1.__len__()
print(l)
for i in range(0, l):
    sum = sum + list1[i]
print("the avg of sum of elements of list is: ", sum / l)

# Ques-5: Read the value from user and number of times to be repeated
a = int(input("Enter a number to print the series: "))
b = int(input("How many times to be printed, enter a number:"))
series = 0
sum = 0
for i in range(0, b):
    series = series * 10 + a
    sum = sum + series
    print(series, end="+")
print("\n The sum of series is:", sum)

# Ques-6: Display the grades of a student
list = []
sum = 0
for i in range(0, 5):
    subjectMarks = int(input("Enter marks for 5 subjects:"))
    list.append(subjectMarks)
for i in range(0, 5):
    sum = sum + list[i]
prcntMrks = sum * 100 / 500
print("Percentage marks of the student is :", prcntMrks)
if 80 <= prcntMrks < 100:
    print("Grade is A+")
elif 70 <= prcntMrks < 80:
    print("Grade is A")
elif 60 <= prcntMrks < 70:
    print("Grade is B+")
elif 60 <= prcntMrks < 50:
    print("Grade is B")
elif 50 <= prcntMrks < 40:
    print("Grade is C")
else:
    print("Improvement needed very less percentage")

''' Ques-7: Printing all the numbers in a range divisible by
a given number'''
r = int(input("enter a range:"))
d = int(input('enter a number to check divisibility:'))
for i in range(0, r):
    if i % d == 0:
        print("Numbers divisible by ", d, "is", i)

# Ques-8: Counting number of digits in a given number
num = int(input("enter a number to count its digits:"))
count = 0
while num > 0:
    rev = num % 10
    num = num // 10
    count += 1
print('Number of digits in the given number is:', count)

# Ques-9: Calculate simple interest
SI = 0
P = int(input("Enter principal amount:"))
r = float(input("enter rate of interest:"))
T = float(input("enter time period:"))
SI = (P * r * T) / 100
print('Simple interest is :', SI)

# Ques-10: Armstrong number(153,370,1634,,8208,54748)
import math

num = int(input("Enter a number:"))
temp = num
pow, rem, a, sum = 0, 0, 0, 0
while num > 0:
    num = num // 10
    pow += 1
num = temp
while num > 0:
    rem = num % 10
    a = math.pow(rem, pow)
    sum = sum + a
    num = num // 10
if sum == temp:
    print("given number", temp, "is a armstrong number")
else:
    print("given number", temp, "is not a armstrong number")

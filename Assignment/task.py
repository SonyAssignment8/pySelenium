#Question 1
#Display numbers that are divisible by 5 and 10
for i in range (50):
    if i%5==0 and i%10==0 :
        print("The numbers divisible by 5 and 10 are :",i)

#Question 2
#get the employee details from the user and display
Emp_no=int(input("Enter the employee number:"))
Emp_name=input("Enter the name of the employee:")
Contact_number=int(input("Enter the contact number of the employee:"))
print("EmplyeeDetails:")
print("Employee number is:",Emp_no)
print("Employee name is :",Emp_name)
print("contact number of employee is :",Contact_number)

#Question 3
s="python for life"
#split the word and display in new line
s=(s.split(" "))
print(s[0])
print(s[1])
print(s[2])

#replace the string
s="python for life"
print(s.replace("life","LIFE"))

#slicing the string
s="python for life"
print(s[2:10])
print(s[11:13])

#replace the string
s="python for life"
print(s.replace("pyhton for life","thon for"))

#convert first and last word to upper
s="python for life"
print(s[0:6].upper(),"for",s[11:15].upper())

#remove last character from a word
s="python for life"
print(s.rstrip('fe'))

#Question 4
#Reverse the string by getting input from user
s=input("Enter a string which is to be reversed")
print('The reverse string is :',s[ : :-1])

#Question 5
for i in range (1,11):
    print(i)

#Question 6
for i in range (5,25):
    if i%3==0:
        print("The number divisible by 3 are:",i)

#Question 7
#Maximum of three numbers
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
if a>b and a>c:
   print("a is Greater")
elif b>c:
    print('b is greater')
else:
    print('c is greater')




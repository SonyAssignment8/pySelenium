#Question 1 WAP to display the num which is div by 5 & 10 from 1-100
for i in range(100):
    if i%5==0 and i%10==0:
        print(i,end=" ")

# Question 2:Read the details from the user and display the same in the console[employee details]
print("======================")
empname=input("enter the employee name")
empId=int(input("enter the employee Id"))
emppf=int(input("enter employee PF number"))
empGender=input("enter employee gender")
print("employee name==>",empname,"emplyeee ID==>",empId,"emplyee PF Num",emppf,"emplyee gender",empGender)
print("============")
#question number 3
print("question 3)a")
print("============")
s="python for life"
sp=s.split()
for i in sp[::1]:
    print(i)

print("Question 3)b")
s1="python for life"
print(s1[2:10])
print("question no 3)c")
print(s1[8:13])
print("question no 3)d")
sp=s1.split()
for i in sp[::1]:
    if i=="life":
        print(i.upper(),end=" ")

    else:
        print(i,end=" ")
print("=========")
print("question no 3)E")
for i in sp[::1]:
    if i=="life" or i=="python":
        print(i.upper(),end=" ")
    else:
        print(i,end=" ")

#Read the i/p string from user and print it in reverse order
print("=========question no 4========")
print("question number 4 answer")
strn=input("enter the string")
rev=strn[::-1]
print(rev)

print("question no 5)write a program to print from 1 to 10")
for i in range(10):
    print(i,end=" ")

print("============")
print("======question num 6========")
for i in range(5,25):
    if i%3==0:
        print(i)

#WAP to find Max of three num
x=20
y=50
z=40
if x>y and x>z:
    print("Greater number is===>",x)
elif y>z and y>x:
    print("Greater number is====>",y)
else:
    print("Greater number is=====>",z)




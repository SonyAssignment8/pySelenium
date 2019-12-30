# d={"class1":{"Name":"divya","Rollnum":100,"Subject":"Maths"},"Class2":{"Name":"divya","Rollnum":100,"Subject":"Maths"}}
# print(5.925//1)
# print(ord('a'))
# print(chr(97))
# l1=[10,20,30]
# l2=[10,20,30]
# print(l1 is l2)
# print(l1==l2)
# print(id(l1))
# print(id(l2))
#print(0 or 20)
# print(0 and 20)
# print(10)
# a=10
# b=20
# c=30 if a>b else 40
# print(c)
# a=int(input("Enter the first number"))
# b=int(input("Enter the second number"))
# c=int(input("Enter the third number"))
# min=a if a<b and a<c else b if b<c else c
# print(min)
# d={'a':'apple','b':'ball','c':'cat'}
# for i in d:
#     print(d[i])
# n=5
# res=1
# for i in range(1,n+1):
#     res=res*i
# print(res)
# n=5
# result=0
# for i in range(1,n):
#    result=result+i
#    print(result)
# a=0
# b=1
# temp=0
# print(a)
# print(b)
# for i in range(2,11):
#    c=a+b
#    a=b
#    b=c
#    print(c)
# Linear search
# a=[10,20,30,40,50,60,70]
# key=500
# flag=0
# for i in range(0,len(a)):
#    if a[i]==key:
#       flag=1
#       break
# if flag==1:
#    print("Elemnet is present")
# else:
#    print("Elemnet not present")
# dynamic insertion
# n=int(input("Enter the size of the list"))
# l=[]
# for i in range(0,n):
#     element=int(input("Enter the elements"))
#     l.append(element)
# print(l)
# n=tuple(input("Enter the elemnets"))
# print(n)
# n=int(input("Enter the size of the dictionary"))
# d={}
# for i in range(0,n):
#     key=int(input("Enter the key"))
#     value=input("Enter the values")
#     d[key]=value
# print(d)
# def disp(n):
#     if n<=0:
#         print(n,end=" ")
#         return
#     print(n,end=" ")
#     disp(n-1)
#     print(n,end=" ")
# disp(9)
#Factorial
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))
#Fibonnacci
def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)
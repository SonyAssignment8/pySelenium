# #1-print first char in file
# f=open("abc.txt",'r')
# print(f.read(1))
# f.close()
#
# #2-count unique words in file
# f1=open("hello.txt",'r')
# l=f1.readlines()
# print(l)
# print("the count of unique words",set(l).__len__())

#read data from file and print in reverse order
file=open("hello.txt",'r')
lines=file.readlines()
print(lines)
lines.reverse()
for w in lines:
    print(w,end=" ")
for i in lines:
    print(i[::-1])

# #calculate average of n numbers in list
# i=int(input("enter how many numbers you mant:"))
# sum=0
# for j in range(0,i):
#     num=int(input("enter numbers:"))
#     sum=sum+num
# avg=sum//i
# print("the average of numbers is:",avg)
#
# #print n+nn+nnn
# s=input("enter number:")
# s1=s+s
# s2=s+s+s
# print(s,'+',s1,"+",s2)
# sum=int(s)+int(s1)+int(s2)
# print("the sum is:",sum)
#
# #student marks ,dipslay grade
# sum=0
# for i in range(0,5):
#     sub=int(input("enter 5 subject marks:"))
#     sum=sum+sub
# avg=sum//5
# print(avg)
# if avg in range(70,80):
#     print("A grade")
# elif avg in range(50,70):
#     print("B grade")
# elif avg in range(40,50):
#     print("C grade")
# elif avg in range(80,100):
#     print("A+ grade")
# else:
#     print("better luck next time")
#
# #print num in range divisible by given num
# s=int(input("enter the starting range:"))
# e=int(input("enter the ending range:"))
# n=int(input("enter the num to divide:"))
# for i in range(s,e):
#     if i%n==0:
#         print(i)
#
# #count num of digits in num
# number=input("enter the number:")
# print(len(number))
#
# #find largest and second largest number in list
# l=int(input("enter how many numbers you want:"))
# list=[]
# for i in range(0,l):
#     n=input("enter the numbers:")
#     list.insert(i,n)
# list.sort()
# print("the largest num is:",list[l-1])
# print("second largest in a list:",list[l-2])
#
# #merge 2 list and sort
# l1=[5,6,4,3,9]
# l2=[7,6,3.2,5,8]
# l1.extend(l2)
# print(l1)
# l1.sort()
# print(l1)
#
# #swap first and last value of list
# print("before swap:",l2[0],l2[4])
# l2[4],l2[0]=l2[0],l2[4]
# print("after swap:",l2[0],l2[4])
#
#
#

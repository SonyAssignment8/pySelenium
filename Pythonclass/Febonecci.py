#febonecci series
# a=0
# b=0
# c=1
# print("Febonecci series is:==>")
# for i in range(8):
#     a=b
#     b=c
#     c=a+b
#     print(a,end=" ")
# print()
# #Factorial of a number
# num=4
# fact=1
# for i in range(num):
#     fact=fact+fact*i
#
# print("factorial of a number is:==>",fact)
# print()

#Given number is palindrome or not
num=121
temp=num
pal=0
while num>0:
    rem=num%10
    num = num // 10
    pal=pal*10+rem
if temp==pal:
    print("given number is palindrome")
else:
    print("given number is not a palindrome")

# find the given number is arm-strong or not


# average of a number from list
num = [1, 2, 3, 4,5]
add = 0
for i in num:
    add = add + int(i)
avg = add / num.__len__()
print(avg)

# Q num 6)

# def sum(unum):
#     total=unum+unum*unum+unum*unum*unum
#     return total
#
#
# unum=int(input("enter the number"))
# print(sum(unum))

# question 7) take the 5 subject marks from student and display the grade like if avg>90=A+ >80=B+,avg<70=c+ avg<50 fail

# ls = []
# for i in range(0, 5):
#     ls.append(int(input("Enter PCMBC marks Respetively")))
#
# total = 0
# for i in ls:
#     total = total + int(i)
# avg = total / ls.__len__()
#
# if avg >= 90:
#     print("Grade==>A+")
# elif 80 <= avg <= 89:
#     print("Grade is B+")
# elif 70 <= avg <= 79:
#     print("Grade is C+")
# elif avg < 50:
#     print("Grade is Fail")

#WAAP to print range of numbers that are divisible by given number
# div=int(input("Enter the number to divide"))
# for i in range(1,20):
#     if i%div==0:
#         print(i,end=" ")

#question 10) count number of digits i a length of numbers
# number=int(input("enter numbers"))
# count=0
# while number>0:
#     number=number//10
#     count+=1
# print(count)

#WAP to find Simple Intrest
# p=float(input("Enter the principle amount"))
#
# t=float(input("Enter the duration in terms number of month"))
# td=t/12
# r=float(input("Enter the rate of interest per Annum"))
# si=p*td*r/100
# print("Interest for",t,"Months is",si)


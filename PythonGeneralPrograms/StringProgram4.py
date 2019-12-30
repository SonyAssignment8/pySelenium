# Q no 21) WAP to remove the nth index character from the non empty string
# str="python"
# ind=int(input("enter the index number"))
# print("Removed the character from index number",ind,"==>",str[ind+1:]+str[:ind])

#Find the length of the string without using library function
# st="python"
# count=0
# for i in st:
#     count+=1

#print("Length of the string is",count)

#Find the number characters and number of words in a string
# strn="hi hello hwo are you"
# words=strn.split().__len__()
# print("Number of words in a string",words)

#find the number of charaters
# strn1="hi hello hwo are you"
# char=strn1.replace(" ","")
# lst=list(char).__len__()
# print("Number of characters in a string",lst)

#take two string and add to 3rd string with string 1 first two characters and and last two chracters from string two
# strin1="python"
# strin2="java"
# strin3=""
# strin3=strin1[0:2:]+strin2[-2::]
# print(strin3)

#WAP to check common letters from two string
# s=input("Enter first string")
# s1=input("Enter second string")
# s3=""
# for i in s:
#     if s1.__contains__(i):
#         print(i,end=" ")

#WAP to display which are in first string but not in second string
# s2="himalaya"
# s4="meghalaya"
# for i in s2:
#     if s4.__contains__(i):
#         print(end=" ")
#     else:
#         print(i,end=" ")

#WAP to display unique charaters from the two string by ignoring duplicates
s5="himalaya"
s6="meghalaya"
for i in s5:
    if s6.__contains__(i):
        print(end="")
    else:
        print(i,end="")
for j in s6:
    if s5.__contains__(j):
        print(end=" ")
    else:
        print(j,end=" ")

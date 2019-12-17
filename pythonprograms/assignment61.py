#read from file and print words and return len of longest word
file=open("hello.txt","r")
words=file.read().split()
print(words)
'''max method returns largest elment in an iterable ,
key fun where the iterables are passed and comparison is performed
based on its return value'''
#returns large word
print(max(words,key=len))
#

# #remove nth index char from from string
s='python is good'
n=int(input("enter index u want to return:"))
s1=s[:n]+s[n+1:]
print(s1)

#detect anagram strings,counter() also can be used
s3=input("enter first string:")
s4=input("enter the second string:")
assert sorted(s3)==sorted(s4),print("not anagrom string")
print("anagrom string:")

# #count number of vowels in string
ocount=0
vcount=0
olist=['a','e','i','o','u']
d=input("enter the string to count the vowels:")
for i in d:
    if i in olist:
        ocount=+1
    else:
        vcount=+1
print(ocount)
print(vcount)

# #read data from file and replace space with _
f=open("hello.txt",'r')
str=f.read().replace(' ','_')
print(str)

# #find length of string without using built in fun
s5='python'
count=0
for i in s5:
    count=count+1
print("the lrngth of string is:",count)

# #find num of words and num of char in string
str6=input("enter the string:")
chara=0
print("the num of words :",len(str6.split()))
for i in str6:
    chara=chara+1
print("the num of charecters:",chara)

#made new string from first 2 and last 2 string
s8='qspider'
s9='jspider'
s10=s8[:2]+s9[:-3:-1]
print(s10)


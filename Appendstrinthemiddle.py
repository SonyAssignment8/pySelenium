# Write a program, Given two strings, you have to insert second string exactly at the middle of the first string
from math import ceil
s1="eigth"
s2="Chennai"
index=ceil(len(s1)/2)
print(index)
res=s1[:index]+s2+s1[index:]
print(res)



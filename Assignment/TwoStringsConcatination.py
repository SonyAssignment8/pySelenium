#29.Write a program, Given two strings, you have to insert second string exactly at the middle of the first string
str1="krishnakumara"
str2="kushi"
s=" "
for i in range(0,len(str1)):
    if i<len(str1)/2:
        s=s+str1[i]
    elif i==len(str1)/2:
        s=s+str2
    else:
        s=s+str1[i]
print(s)

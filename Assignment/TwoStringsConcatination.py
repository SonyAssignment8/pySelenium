#29.Write a program, Given two strings, you have to insert second string exactly at the middle of the first string
str1="i india"
str2="love"
index=str1.find("india")
print(str1[:index]+str2+" "+str1[index:])

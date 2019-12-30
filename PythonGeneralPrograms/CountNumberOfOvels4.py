#count the number of vowels
str="aeiou"
count=0
vowels="aeiouAEIOU"
for i in str:
    if vowels.__contains__(i):
        count+=1

print("number of vowels present in a given string is",count)

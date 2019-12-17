str1=input("Enter first string")
str2=input("Enter second  String")
def isAnagram(str1,str2):
    return  sorted(str1)==sorted(str2)

if isAnagram(str1,str2):
    print("Anagram")
else:
    print("Not Anagram")

print(sorted(str1))
print(sorted(str2))
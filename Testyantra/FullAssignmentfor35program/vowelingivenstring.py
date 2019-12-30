string = input("Enter string:")
vowels=0
o = len(string)
print("Length of a string are: ", o)
print()
for p in string:
 if(p=='a' or p=='e' or p=='i' or p=='o' or p=='u' or p=='A' or p=='E' or p=='I' or p=='O' or p=='U'):
  vowels = vowels+1
print("Number of vowels are:")
print(vowels)
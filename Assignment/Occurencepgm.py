#To find the occurence of the string
#One way
s=input("Enter a string to count occurence :")
d={}
count=1
s.replace(' ','')
for char in s:
    d[char]=d.get(char,0)+1
print("Character dict for '{}' is :\n {}".format(s,str(d)))
#Other Way
str=
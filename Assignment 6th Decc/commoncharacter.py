#WAP to check common letters in two strings
s1=input('Enter the string1')
s2=input('Enter the string2')
l=[]
l1=list(s1)
l2=list(s2)
l.extend(l1)
l.extend(l2)
s=set(l)
if len(l)!=len(s):
    print('Common letters are present in the strings')
else:
    print('Common letters are not present in the strings')


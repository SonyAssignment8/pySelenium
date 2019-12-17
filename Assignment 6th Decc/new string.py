#WAP to form a new string made of first two and last two characters
s1=input('Enter the first string')
s2=input('Enter the second string')
l=[]
fchar=s1[0]
schar=s1[1]
lchar=s2[-1]
lbchar=s2[-2]
l.append(fchar)
l.append(schar)
l.append(lbchar)
l.append(lchar)
s1=''.join(l)
print('The new string is:',s1)

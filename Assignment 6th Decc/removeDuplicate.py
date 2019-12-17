#Wap to display the remaining string present in second string by removing duplicates
s1=input('Enter the string 1')
s2=input('Enter the string 2')
l=[]
l1=[]
l.extend(s1)
l.extend(s2)
l.sort()
print(l)
s=set(l)
print(s)
for i in range(0,len(l)):
        if l[i]!=s:
            l1.append(l)
print(l1)





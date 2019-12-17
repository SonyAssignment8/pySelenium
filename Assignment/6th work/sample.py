#Deep Copy
l1=[1,2,3,4]
l2=l1
print(l2)
l1.append(10)
print(l1)
l2.append(20)
print(l1,l2)
l2.pop()
print(l2)

#Shallow copy
a=[1,2,3,4]
b=a.copy()
a.append(5)
print(a)
print(b)

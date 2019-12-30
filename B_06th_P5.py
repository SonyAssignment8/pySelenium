#Deep Copy
l=[1,4,5]
l1 = l
l.append(6)
print("l",l)
print("l1",l1)
l1.pop()
print("------")
print("l",l)
print("l1",l1)

#Shallow copy
a= [1,2,3,4]
b = a.copy()
a.append(5)
print("a",a)
print("b",b )
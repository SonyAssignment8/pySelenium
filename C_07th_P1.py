#nested list
l=[1,2,['hi','hello',2.4,3],5]
print(l[2][1][1])
print(l[2])
print(l[2][1])
l.append(4)
print(l)
l[2].insert(1,"GM")
print(l)
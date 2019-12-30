lst = [1, 2, 3, 4]
r=iter(lst)
for i in range(lst.count(r)):
    lst.append(r)
print(r)



list1 = [1,2,3,4,1,2,1,2]
print(list1)
set = {None}
for i in range(1,8):
    a = list1[i]
    set.add(a)
print(set)

list2 = [1,2,3,4,1,2,1,2,8,9]
l= []
for i in range(0,len(list2)):
    l.append(list2[i])
    if (list2.count(list2[i])>1):
        l.pop()
print(l)








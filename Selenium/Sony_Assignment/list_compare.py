# 15. Write a program to store the element present in list1 and not in list2
lst1 = [1,4,5,6,9]
lst2=[3,6,10,11]
lst3 = []
for i in lst1:
    if i not in lst2:
        lst3.append(i)
print(lst3)
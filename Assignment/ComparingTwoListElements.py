#15. Write a program to store the element present in list1 and not in list2
lst1=[1,2,4,5,6,7]
lst2=[4,5,6,8,9,2]
for i in lst1:
    if i not in lst2:
        print(i)

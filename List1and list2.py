# Write a program to store the element present in list1 and not in list2
list1=[10,20,30,40,50]
list2=[1,2,3,4,5]
#Listcomprehension to print numbers in list 1 and not in list 2
print([x for x in list1 if not x in list2])
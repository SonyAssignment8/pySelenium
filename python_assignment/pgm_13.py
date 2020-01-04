# 15. Write a program to store the element present in list1 and not in list2
l1=[11,2,3,4,5,6]
l2=[1,6,8,91,2,3]
a=set(l1)
b=set(l2)
print(list(a.difference(b)))
# if len(b.difference(a)) > 0:
#         print(b)
# else:
#     print("not in list 2")



#merge tow list into one list
l1=[2,3,1,56,78]
l2=[4,89,45,67,2,1]
l2.extend(l1)
print("===Before sort===")
print(l2)
l2.sort()
print("===After sort===")
print(l2)
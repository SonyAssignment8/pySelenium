# 38. From a list copy all the even and odd numbers in separate lists in sorted order
l=[1,2,4,6,7,9,3]
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even list",even)
print("odd list",odd)
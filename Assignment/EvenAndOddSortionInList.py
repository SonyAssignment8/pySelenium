#38. From a list copy all the even and odd numbers in separate lists in sorted order.
lst=[10,1,3,4,5,6,7,8,9,7,20,26,25]
even=[]
odd=[]
for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

even.sort()
odd.sort()
print(even)
print(odd)
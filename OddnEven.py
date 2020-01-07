# From a list copy all the even and odd numbers in separate lists in sorted order.
l=[10,21,33,67,80,30]
even_list=[]
odd_list=[]
for i in range(0,len(l)):
    if l[i]%2==0:
        even_list.append(l[i])
        even_list.sort()
    else:
        odd_list.append(l[i])
        odd_list.sort()

print("Even list is :",even_list)
print("Odd list is:",odd_list)

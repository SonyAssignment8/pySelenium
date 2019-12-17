#swap first and last element of the list
l=[10,20,30,40,50,60]
i=len(l)
temp=l[0]
l[0]=l[i-1]
l[i-1]=temp
print(l)

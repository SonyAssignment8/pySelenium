l=[2,3,6,4,10,12,13,14,1]
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
even.sort()
odd.sort()
print(even)
print(odd)
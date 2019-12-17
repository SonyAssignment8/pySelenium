class odd():
    l=[10,21,34,67,89,90]
    print(len(l))
    even=[]
    odd=[]
    for i in range (0,len(l)):
        if (l[i]%2)==0:
            even.append(l[i])
        else:
            odd.append(l[i])
    print(even)
    print(odd)

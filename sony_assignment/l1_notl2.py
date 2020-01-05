l1=[2,3,6,4,1,8]
l2=[2,3,9,10,11,12]
l3=[]
for i in l1:
    if i not in l2:
        l3.append(i)
print(l3)


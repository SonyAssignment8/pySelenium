#intersect and unoin
l1=[1,6,2,7,8,3,7,6,1]
l2=[5,2,2,6,4,9,3]
l3=[]
l4=[]
def intersect(l1,l2):
     for i in l1:
         if i in l2 :
             if i not in l3:
                 l3.append(i)
     return l3
def unionlist(l1,l2):
    for i in l1:
            if i not in l4:
                l4.append(i)
    for i in l2:
            if i not in l4:
                l4.append(i)
    return l4
print("intersection list is:",intersect(l1,l2))
print("union list is:",unionlist(l1,l2))


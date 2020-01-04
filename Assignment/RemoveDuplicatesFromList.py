#Write a code to remove the duplicate from a list.
lst=[1,2,4,5,3,2,3,5,8]
newlist=[]
for i in lst:
    if i not in newlist:
        newlist.append(i)

print(newlist)

l=[2,2,3,1,4,6,1,3]
s=set(l)
print(s)
li=[]

#without using built in function
for i in l:
    if li.__contains__(i):
        print()
    else:
        li.append(i)
print(li)

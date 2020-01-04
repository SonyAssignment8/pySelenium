# 26.  l=[1,2,3,4,5], output = 5  create a list which will have the indexes of elements e.g. 1+4=5,2+3=5 so get the index of the elements which will give the output
	# L=[(0,3),(1,2)]

l=[1,2,3,4,5]
print(l[0]+l[3])
print(l[1]+l[2])
print(l[-1])
a=l.index(1)
b=l.index(4)
c=l.index(2)
d=l.index(3)
l1=[(a,b),(c,d)]
print(l1)

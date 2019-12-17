#swap first and last elements in a list
l1=[2,3,4,5,6,0,1]

print("============Before swap==========")
print(l1)

print("==========After swap==========")

l1[0],l1[-1]=l1[-1],l1[0]
print(l1)

lst=[2,7,8,9,1,6,1,3]

#sorting in ascending order
for i in range(0,len(lst)):
    for j in range(0,len(lst)):
        if lst[i]<lst[j]:
            lst[i],lst[j]=lst[j],lst[i]

#sorting in decending order
for i in range(0,len(lst)):
    for j in range(0,len(lst)):
        if lst[i]>lst[j]:
            lst[i],lst[j]=lst[j],lst[i]

print(lst)


#34. Write a code to swap elements.
a=20
b=30
a,b=b,a
print("a value after swaping is",a,"==","b value afte swaping is ",b)





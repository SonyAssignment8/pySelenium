#Write a code to sort elements present in list (without using built in method)
list=[80,30,20,90,100]
for i in range(0,len(list)):
    for j in range(0,len(list)):
        if list[i]<list[j]:
            list[i],list[j]=list[j],list[i]
print(list)

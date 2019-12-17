

#to copy the data from one file into another file
f=open("ab.txt")
f1=open("ab12.txt","a")
count=1
sum=0
alpha=1;
alpsum=0
for list in f.readlines():
    f1.write(list)
    print("length of the charectors in each line",len(list))
    total=len(list)
    count+=1
    if list.isalpha():
        alpha+=1

sum=sum+count
print("Total no of line  is",sum)
print("total no of Charectors is ",total)
f.close()
f1.close()















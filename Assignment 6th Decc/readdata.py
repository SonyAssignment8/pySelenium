#read data from the file and print the length of the longest one
f=open('f.txt','r')
l1=[]
data=f.readlines()
for i in range(0,len(data)):
    data[i]
    l= len(data[i])
    print(l)
    l1.append(l)
print('The length of the longest word is:',max(l1))


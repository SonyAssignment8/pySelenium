#Question 11 a)
f1=open("File1.txt","r")
#data=f1.readline()  #Reading from file 1

# f2=open("File2.txt","w")
# f2.write(data) # writing to file 2
# f2.close()

#count number of charaters from file 1

# d=f1.read().replace(" ","").__len__()
# print(d)

#number of words from file1

d1=f1.read().split()
c=d1.__len__()
print("number of words in the file1",c)
f1.close()


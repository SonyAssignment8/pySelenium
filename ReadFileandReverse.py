#Program to read a file and reverse each line
#Write data in file
f=open('file.txt','w')
f.write('Hello to world')
f.close()

#Read data from file
f=open('file.txt','r')
data=f.read()
print(data[::-1])

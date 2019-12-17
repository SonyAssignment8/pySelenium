#to read the data use for loop
f=open("file.txt","r")
data=f.read()
f.close()
f=open("file1.txt","w")
f.write(data)
f.close()
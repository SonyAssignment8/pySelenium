#read first character from the file
readFile=open('f.txt','r')
data=readFile.read()
print(data[0])
readFile.close()

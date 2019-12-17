#Read data from the file and replace all the blank space to '-'
f=open('f.txt','r')
data=f.readlines()
for i in range (0,len(data)):
    newdata=data[i].replace(" ","-")
    print(newdata)
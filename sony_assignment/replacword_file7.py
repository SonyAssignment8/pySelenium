f=open("f2.txt",'r')
#read full file and replce
data=f.read()
new=data.replace("good","bad")
#before writing into file we must close the file
f.close()

#then again open in w mode
f3=open("f2.txt",'w')
f3.write(new)
#program to replace a specific word in a file
f=open("TextFile.txt","r")
actual=f.read().replace("xyz","How")
print("after replacing ",actual)





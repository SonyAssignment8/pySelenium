#7. Write a program to replace the specific words in a file?
f=open("f1.txt","r")
data=f.read()
print("replace the specific words in a file:",data.replace("python","java"))
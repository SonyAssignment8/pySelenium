#. Program to read a file and count occurrence of each word?
f=open("TextFile.txt","r")
str=f.read()
di={}
sp_word=str.split(" ")
for i in sp_word:
    di.setdefault(i,sp_word.count(i))

print(di)

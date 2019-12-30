#Q 1)print 1st charater in a string
f=open("File1.txt","r")
data =f.read()
# print(data[0])

# Q2)count unique words in a file
# sp=data.split()
# st=set(sp).__len__()
# print("number of unique words in file ",st)

#Q 4) print file data in reverse order
print(data[::-1])
# Q5)
# 20 read the data from file and print the words and return the length of longest word
# print(data)
# l=[]
# splt=data.split()
# for i in splt:
#     l.append(i.__len__())
# l.sort()
# print("highest length of the word is",l[-1])

#Read Data from file and Replace space with '-'
print(data.replace(" ","-"))
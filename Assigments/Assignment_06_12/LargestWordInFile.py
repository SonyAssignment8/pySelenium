# Ques-17
f = open("xyz.txt", "w")
f.write("The random module provides access to functions that support these"
        "types of operations asdfghjklzxcvbnm")
f.close()
f = open("xyz.txt","r")
data = f.readlines()
l = data[0].split(" ")
max = 0
for i in l:
        if i.__len__() > max:
                max = i.__len__()
print("The length of longest word in the file is:",max)



# Writing data into a file
file = open("abc.txt",'w')
file.write("My name is Jyoti Sahu Sahu")
file.close()

# Reading data into a file
file = open("abc.txt",'r')
data = file.read()

# Ques-1: Displaying first character of the file
print("First character of the file is :",data[0])

# Ques-2: Counting unique number of words in a file
s = data.split()
SET = set(s)
print("Number of unique words in file is:",SET.__len__())
file.close()

# Ques-3(a): Reversing all words of the file
str1 = ' '.join(reversed(data.split(' ')))
print("Reverse of words of the file data is :",str1)

# Ques-3(b):Reversing all characters of the file
print("Reverse of characters of the file data is:", data[::-1])


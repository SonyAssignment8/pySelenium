# Writing data into file
f = open("ab.txt","w")
f.write("hello world \n  My name is jyoti sahu \n Married to dhanendra sahu")
f.close()

# Reading the data from a file
f = open("ab.txt","r")
data = f.read()
print(data)
f.close()

# append any data at the end of the file
f = open("ab.txt","a")
f.write("\n This is my world")
f.close()
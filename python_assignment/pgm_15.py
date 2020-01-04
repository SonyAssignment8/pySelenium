# 17. Program to read a file and count occurrence of each word?
f=open("f1.txt","r")
# d=f.read()
d = dict()


for line in f:
    # Remove the leading spaces and newline character
    line = line.strip()
    line = line.lower()

    # Split the line into words
    words = line.split(" ")

    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:

            d[word] = d[word] + 1
        else:

            d[word] = 1

# Print the contents of dictionary
for key in list(d.keys()):
    print(key, ":", d[key])
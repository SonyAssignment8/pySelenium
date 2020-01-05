# 7. Write a program to replace the specific words in a file
fileName = input("Enter a file name:")
rplce_word = input("Enter a word to be replaced in file:")
rplce_word_with = input("Enter new word as replacement of old:")
f1 = open(fileName, 'r')
fileData = f1.readlines()
for i in fileData:
    strng = i.replace(rplce_word,rplce_word_with)
    print(strng)



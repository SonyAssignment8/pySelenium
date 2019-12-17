#To print file data in reverse order
f=open('f.txt','r')
datalines=f.readlines()
print(datalines)
reverse=''.join(reversed(datalines))
print(reverse)
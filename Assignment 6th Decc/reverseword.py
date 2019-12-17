#reverse all word character in the file
f=open('f.txt','r')
data=f.read()
reverse=''.join(reversed(data))
print(reverse)
print('=====================')
#reverse the line in file
f=open('f.txt','r')
data=f.readlines()
for i in range(0,len(data)):
    word=data[i]
    print(word[ : :-1])




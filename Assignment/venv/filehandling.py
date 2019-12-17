f=open('f.txt','w')
f.write('hi')
f.close()

f=open('f.txt','a')
f.write('\tHello to the world')
f.close()

f=open('f.txt','r')
data=f.read()
print(data)
f.close()
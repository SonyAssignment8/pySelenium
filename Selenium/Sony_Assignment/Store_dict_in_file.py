# 8.to store dictionary values in a file
animalDict = {1:"Horse",2:"Lion",3:"Tiger",4:'Fox',5:'Zebra'}
f1 = open("animal.txt",'w')
f1.write(str(animalDict))
f1.close()

f1 = open("animal.txt",'r')
data = f1.readlines()
print(data)
f1.close()
#how to store dictionary values in an external file
d ={1:"hi",2:"hello",3:"how",4:"are",5:"you"}
f=open("TextFile2.txt","w")
f.write(str(d.values()))
print("written successfully...")
f.close()
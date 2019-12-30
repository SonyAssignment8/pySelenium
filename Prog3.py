#3.Read the data from file & print 7 lines of the file (10 lines read)
f = open("demo.txt","r")
for i in range(1,8):
    data = f.readline()
    print(data)
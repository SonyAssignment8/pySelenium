Python={"Akshay":"python","Superman":"python","Spidy":"python"}
Javascript={"X":"js","Y":"js"}
sdet={"A":"sd","B":"sdss"}
print("1.Python")
print("2.Javascript")
print("3.SDET")
course=int(input("Select Your course:"))
if course==1:
    print(Python.keys())
elif course==2:
    print(Javascript.keys())
else:
    print(sdet.keys())


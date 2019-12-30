#Add key value pair to the dictionary
d={}
d.setdefault(1,"krishna")
d.setdefault(2,"kushal")
d.setdefault(3,"khushi")
print(d)

#heck weather the given key is present or not
# ky=d.keys().__contains__(int(input("enter the key to search")))
# print("The entered key is present:==>",ky)

#WAP to generate a dictionary that contains a number from 1 to n in the form of a:a*a
di={}

for i in range(0,4):
    x = int(input("enter the number"))
    di.setdefault(x,x*x)

print(di)


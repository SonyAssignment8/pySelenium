#2.To count the unique words in a file(use set)
# f=open("a_new.txt","w")
# f.write("one two two")
# f.close()
#
# f=openf=open("a_new.txt","r")
# data=f.read()
# print(data)
unique = set(["one","two","two","three","three"])
print(len(unique))
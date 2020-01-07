#Display names in alphabetical order?
size=int(input("Enter the number of names you want to enter: "))
l=[]
for i in range(0,size):

   input_str = input("Enter a string: ")
   l.append(input_str)
# sort the list
   l.sort()

print("The sorted words are:")
for word in l:
   print(word)
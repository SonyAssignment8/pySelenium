#Program to reverse list of string
str=["hi","helo","revanna","sir","how","your","in","which","home"]
#print(str[::-1])   #one way is using slicing

#without using slicing
for i in range(0,len(str)):
    print(str[len(str)-1-i],end=" ")



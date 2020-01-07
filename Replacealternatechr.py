# Replace every alternate character in a string with a “*” using inbuilt function and without using inbuilt function
#by using inbuilt method
s="Apples"
str=s[0: :2]
res="*".join(str)
print(res)

#Without using inbuilt method
str="Bangalore"
s=" "
j=0
for i in range(0,len(str)):
    if j<=len(str):
        s=s+str[j]+"*"
        j+=2
print(s)




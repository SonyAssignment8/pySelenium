#26 Replace every alternate character in a string with a “*” using inbuilt function and without using inbuilt function
# str="bengalore"
# # s=str[::2]
# # new_s="*".join(s)
# # print(new_s)

#without using inbuilt function
str="bengalore"
s=" "
j=0
for i in range(0,len(str)):
    if j<=len(str):
        s=s+str[j]+"*"
        j+=2

print(s)



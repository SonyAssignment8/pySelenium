str1="sujitha"
str2="bhavaneesh"
str3=""
str4=""
for i in str1:
    for j in str2:

        if i==j:
            str3=str3+j
        else:
            str4=str4+j


print("Coomon characters in two string",str3)
print("Which is not common in two strings",str4)
str1="Qspider"
str2="Jspider"
str3=""
for i in str1:
    if i in str2:
        print(end=" ")
    elif i not  in str2:
        print(i,end=" " )
        for j in str2:
            if j in str1:
                print(end=" ")
            elif j not in str1:
                print(j,end=" ")
# for i in  str1:
#     for j in  str2:
#         if i == j:
#           str3=str3+j

print(str3)
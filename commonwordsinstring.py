str1 =input("Enter first string")
str2 =input("Enter second string")
s1=str1.split(" ")
s2=str2.split(" ")
s3=""
s4=""
for i in s1:
    for j in s2:
        if i==j:
            s3=s3+j+" "
        elif i!=j:
            s4=s4+j+" "


print("Common words---",s3)
print(s4)
#
# for i in str1:
#     if i in str2:
#         print(end=" ")
#     elif i not  in str2:
#         print(i,end=" " )
#         for j in str2:
#             if j in str1:
#                 print(end=" ")
#             elif j not in str1:
#                 print(j,end=" ")





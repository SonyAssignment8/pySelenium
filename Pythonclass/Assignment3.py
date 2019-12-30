#to remove duplicates from list
list=[1,2,3,4,1,2,1,2]
res=[]
for i in list:
    if i not in res:
        res.append(i)
print("without dupliates",res)

#Question number 2
arrlist=[32,4,5,1,6]
arrlist.sort()
x=arrlist.copy()
y=x[::-1]
print("decending order",y)  #decending order


#Question 3) load integer object to lis and get the total sum of list

al=[]
for i in range(0,5):
    al.append(input("Enter numbers into array"))
sum=0;
for j in al:
    sum=sum+int(j)
print(sum)

#question number 4)
# plist={"krishna":"python","rashmi":"python","sujitha":"python","divya":"python","jyoti":"python"}
# jslist={"sasmitha":"javascript","pankaj":"javascript","prakash":"javascript"}

plist={"krishna":"python","rashmi":"python","sujitha":"python","divya":"python","jyoti":"python","sasmitha":"javascript","harika":"javascript","prakash":"javascript"}
num=input("Press 1 for Python employee list and press 2 for javasript employees")
if num=="1"or num=="python" or num==2 or num=="javascript":
    v=plist.values()
    if v.__eq__("python") or num==1:
        print("PYTHON EMP LIST",plist.keys())
    elif v.__eq__("javascript") or num==2:
        print("JAVA SCRIPT EMP LIST",jslist.keys())

# Question number 5)
str="Hi All123 How are$y@&ou Python Team"
sp=str.replace(" ","")
dig=0
upp=0
low=0
spc=0;
for i in sp:
    if i.isdigit():
        dig+=1
    elif i.islower():
        low+=1
    elif i.isupper():
        upp+=1
    else:
        spc+=1
print("Total number of digits",dig)
print("Total no of upper case letters",upp)
print("Total number of lower case letters",low)
print("Total number of special characters",spc)










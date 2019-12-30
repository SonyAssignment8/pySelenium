str="234"
num=0
for i in str:
    num=num*10
    num=num+ord(i)-ord("0")
print(num)
print(ord("0"))
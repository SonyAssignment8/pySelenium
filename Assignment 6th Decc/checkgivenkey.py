#WAP to check if given key exists in a dictionary or not
userkey=int(input('Enter the key'))
d={1:'AAA',2:'BBB',3:'CCC',4:'DDD'}
k=d.keys()
l=list(k)
flag=False
for i in range(0,len(l)):
     if l[i]==userkey:
        flag=True
     else:
         flag=False
if(flag==True):
    print('Key is present')
else:
     print('Key is not present')


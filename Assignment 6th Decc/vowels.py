#WAP to count the vowels present in the string
l1=['a','e','i','o','u']
s=input('Enter the string')
s=s.lower()
l=[]

for i in range(0,len(l1)):
    count = 0
    for j in range(0,len(s)):
        elements = s[j]
        l.append(elements)
        if(l1[i]==l[j]):
            count+=1
    print('The occurence of vowels in given string',l1[i],'is:',count)
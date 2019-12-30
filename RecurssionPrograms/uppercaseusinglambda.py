#upper case to lower case
str=['A','B']
print(list(map(lambda s:chr(ord(s)+32),str)))

#from lower case to upper case
str1=['a','b','c']
print(list(map(lambda c:chr(ord(c)-32),str1)))

str="krishnakumara"
str2="prakash"
#print([i for i in str if i not in str2 ]and[j for j in str2 if j not in str])

def remove_duplicate(str):
    for i in str:
        if i not in str:
            print(i,end=" ")

remove_duplicate("krishnakumara")




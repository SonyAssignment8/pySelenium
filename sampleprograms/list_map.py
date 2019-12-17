#print number of prime numbers between 50 -150
def isPrime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        return True

print(list(filter(isPrime,range(10,30))))

#filter all the square numbers between the given number
import math
def perfect_sqr(n):
    sqrt_num=int(math.sqrt(n))
    return sqrt_num*sqrt_num==n
print(list(filter(perfect_sqr,range(1,20))))

#list of string to uppercase
# print(list(map(lambda s:s.upper(),'abcde')))
def specialchar(s):
    for i in s:
       if not i.isdigit() and not i.isalpha():
        return i

#specialchar('addh33##$$')
#filter special symbols present in string
#-s='dds#$#$#4534'
print(list(filter(lambda ch:(ch in '@#$%^&*()_+-/*'),'pdfh66$#%$$%')))
print([i for i in 'fhgfg#@$#$' if not i.isdigit() and not i.isalpha()])

def remove_dup(s):
    st=''
    if s not in st:
            st=st+s
    return st
remove_dup('aaabbbccc')

#filter duplicates in string
string='ghghhki'
st=''
print(set(filter(lambda s:s in string,'ghghhki')))

# #filter special symbols present in string
print(list(filter(lambda i:i>='A' and i<='Z' or i>='a'and i<='z','fsf$##$#9043')))



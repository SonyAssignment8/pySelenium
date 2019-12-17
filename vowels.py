vowels="aeiou"
str="This is my pen"
s=""
s2=""
for i in vowels:
    for j in str:
        if i==j:
            s=s+j
            s2=s2+i


if s==s2:
    print("These string contains vowels")
else:
    print("These string does not contains vowels")
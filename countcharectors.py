# input string here
s = input("Input a String: ")
d={"UPPER CASE":0,"LOWER CASE":0,"Digit":0,"Alpha":0}
for c in s:
    # checks whether the character is uppercase or not
    if c.isupper():
        d["UPPER CASE"]+=1
        # checks whether the character is lowercase or not
    elif c.islower():
        d["LOWER CASE"]+=1
        # checks whether the character contains number or not
    elif c.isdigit():
        d["Digit"]+=1
    else:
        d["Alpha"] += 1


#alphabet
print("Number of Uppercase Characters:",d['UPPER CASE'])
print("Number of Lowercase Characters:",d['LOWER CASE'])
print("Number of Numbers Characters:",d['Digit'])
print("Number of Special charectors Characters:",d['Alpha'])

#question 10) revrese a string and print multiple times
str="hello"
for i in range(0,5):
    for j in str[::-1]:
        print(j,end=" ")
    print()
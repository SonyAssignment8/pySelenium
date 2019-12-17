row=5
count=1
space=1
for i in range (1,5,1):
    for j in range (1,5,1):
        print(' ',end=' ')
        for k in range (0,i,1):
            print(k,end=' ')
            j-=1
    print()
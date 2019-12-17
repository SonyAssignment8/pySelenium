#n+nn+nnn+.....series
n=int(input('Enter the value of n'))
m=int(input('Enter the no of times we want the series'))
series=0
sum=0
for i in range(0,m):
    series=series*10+n
    sum=sum+series
    print(series,'+',end=' ')
print('\nThe sum of series is',sum)


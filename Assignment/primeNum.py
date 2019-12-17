class Prime():
    count=0
    x=int(input('Enter the value:'))
    for i in range (50,1,-1):
        if x%i==0:
           count+=1
    if count==2:
        print('The given number is prime')
    else:
        print('The given number is not a prime')
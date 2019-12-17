# filter
# if result is true it hold teh value else its discard the value

def iseven(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
def even_numbers(l):
    even = []
    for i in l:
        if iseven(i):
            even.append(i)
    return even

# filter("adress of function return bolean , collection")
# so instaed of above all exp we can use beow ex :
  print((list(filter(lambda  n:n%2==0 , [1,2,3,4,5,6]))))  # a single line code that reduce all above code


# checking perfect squares from a given list
import math
def perfectSqr(x):
    sr = math.sqrt(x)
    # If square root is an integer
    return (sr - math.floor(sr)) == 0
print(list(filter(perfectSqr, range(0, 26))))

# convert given list of strings to uppercase
print(list(map(lambda i: i.upper(), ['my','name', 'is', 'jyoti', 'sahu'])))

# Filtering special characters from given string
print(list(filter(lambda i: i>='A' and i<='Z' or i>='a'and i<='z','jy#ot%igmail.com')))

# filtering duplicate values from the given string
s = 'asssshhhhhhuuuuu'
print(set(filter(lambda i : i in s,'asssshhhhhhuuuuu')))






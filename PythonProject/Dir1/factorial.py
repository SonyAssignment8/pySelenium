import math
print(math.factorial(5))

#Factorial of a  number
from math import factorial
print(factorial(10))

# To get any particular month from a year
import calendar
print(calendar.month(2019,12, 3))

# Returns number of the given month
print(calendar.February)

import calendar as c
print(c.day_name)
print(c.day_abbr)

# Return number of days in all months
print(c.mdays)

# to check leap year or not
print(c.isleap(2019))

#To print random numbers
import random
for i in range(5):
    print(random.randint(20,30))

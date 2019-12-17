# User enters the year

# The year can be evenly divided by 4;
# If the year can be evenly divided by 100, it is NOT a leap year, unless;
# The year is also evenly divisible by 400. Then it is a leap year.

year = int(input("Enter Year: "))
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 400 ==0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

# or we can do like this
year = int(input("Enter year to be checked:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")
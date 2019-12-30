#leap Year program
year=int(input("Enter The Year"))
if year%4==0 and year%100!=0:
    print("The given year is leap year")
elif year%100==0:
    print("given year is not leap year")
elif year%400==0:
    print("The given year is a leap year")
else:
    print("Year is not a leap year")

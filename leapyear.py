year=2004
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("These is leap year")
        else:
            print("Not leap year")
    else:
        print("Not leap year")
else:
    print("Not leap year")
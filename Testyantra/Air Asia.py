class AirAsia ():
    Searchwithdate = 'Search'
    departuredate = 'depart date'
    arrivaldate = 'Arrival date'
    location = 'location'
    price = 'price'
    timing = 'timing'

    def searchwithdate(self):
     sel= input("Please enter your date" "\n" " 1. Today" "\n" " 2. Tomorrow")

     print(sel)


    def departdate(self):
        sel = input("Please enter depart date" "\n" "1. Today" "\n" "2. Tomorrow")
        print(sel)

    def location(self):
        sel = input( "Please enter location " "\n" "1. Mumbai" "\n" "2. Banglore"  "\n" "3. Pune" "\n" "4. chennai")
        print(sel)

    def price(self):
        sel = input("Please enter Price " "\n" '5000 to 6000' "\n"   '6000 to 7000'  "\n"  '7000 to 8000' "\n" )
        print(sel)
    def timing(self):
        sel = input("Please enter Timing " "\n" " 1. 6 AM to 9 AM" "\n" " 2. 9 AM to 12 AM"  "\n" " 3. 12 PM to 3 PM" "\n" " 4. 3 PM to 6 PM")
        print(sel)



a= AirAsia ()
a.searchwithdate()
a.departdate()
a.location()
a.price()
a.timing()




'''This code allows the user to book a hotel,reschedule the hotel for particular dates
and also to cancell the room bookings'''
class Book():
    #Execute GRT Hotel method
    roomAvailable = 15
    charges = 1000
    tax = 200
    def GRT(self):
        room=int(input('Enter the number of rooms to be booked:'))
        self.roomAvailable=self.roomAvailable-room
        print('No of rooms Available:', self.roomAvailable)
        print('Room charges are:',self.charges*room)
        roomcharges=(self.charges*room)+self.tax
    #Execute Hyaat Hotel method
    def Hyaat(self):
        # roomAvailable = 18
        # charges = 1200
        # tax = 240
        room = int(input('Enter the number of rooms to be booked:'))
        roomAvailable = self.roomAvailable - room
        print('No of rooms Available:', roomAvailable)
        print('Room charges are:', self.charges*room)
        roomcharges = (self.charges*room) + self.tax
    #Execute GreenLand Hotel Method
    def GreenLand(self):
        # roomAvailable = 12
        # charges = 1500
        # tax = 250
        room = int(input('Enter the number of rooms to be booked:'))
        roomAvailable = self.roomAvailable - room
        print('No of rooms Available:',self.roomAvailable )
        print('Room charges are:', self.charges*room)
        roomcharges = (self.charges*room) + self.tax
     #Book the hotels for a particular date
    def Booking(self):
        Arr_date = input('Enter the Arrival date')
        Return_date = input('Enter the Return Date')
        location = input('Enter the location')
        bookingNumber=100
        print('The List of Hotels Available are ')
        print('GRT')
        print('Hyaat')
        print('GreenLand')
        Hotel1 = input('Enter the Hotel name')
        if Hotel1 == 'GRT':
            print('Welcome to GRT')
            self.GRT()
        elif Hotel1 == 'Hyaat':
             print('Welcome to Hyatt')
             self.Hyaat()
        elif Hotel1 == 'GreenLand':
             print('Welcome to GreenLand')
             self.GreenLand()
        else:
            print('Enter the correct Hotel name')
        print('Your booking number is',bookingNumber)
        print('Your room booking is done from ',Arr_date,'to',Return_date)
        bookingNumber+=1
    #cancel the hotel for the particular date
    def cancellation(self):
        bookingNumbe=100
        roomcharges=1000
        cancel=int(input('Enter the Booking number to be cancelled'))
        roomcharges=roomcharges*0.20
        print('The refunded amount is :',roomcharges)
        print('Your ticket has been successfully cancelled')
    #reschedule the hotel for particular dates
    def reschedule(self):
         print('Enter the new dates for which you want to reschedule the ticket')
         Arr_date=int(input('Enter the arrival date'))
         Dep_date=int(input('Enter the departure date'))
         print('Your rescheduled date is :',Arr_date,'to',Dep_date)

# o=Book()
# o.Booking()
# o.cancellation()
# o.reschedule()






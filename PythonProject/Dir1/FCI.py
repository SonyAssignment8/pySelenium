"""FCI stands for Food Corporation of India, mainly it deals with all the sale and purchase of crops after every
cropping season. Before every crop harvest government declares a fixed MSP(Minimum Sale Price) for each crop. Benefit
of declairng MSP before harvest is that farmers will never be in loss in any case at least they will get their
investment amount """


class FoodCorpInd():
    FarmerName = input("Enter Farmer name:")
    location = input("Enter loaction:")
    mob = int(input("Enter contact number:"))
    crop = input("Enter crop name:")
    Qty = int(input("Enter quantity for crop:"))
    price = int(input("Enter price for crop:"))

    def sale(self):
        if self.crop == 'wheat':
            print('MSP for wheat(100kg) is Rs.2300')
        elif self.crop == 'rice':
            print('MSP for rice(100kg) is Rs.2000')
        elif self.crop == 'bajra':
            print('MSP for bajra(100kg) is Rs.1850')
        else:
            print("MSP for the crop " + self.crop + 'is Rs.1500')

    def totalPrice(self):
        print('Total price for the crop sold is ',self.Qty*self.price)

    def farmerDetails(self):
        print("Farmer:", self.FarmerName, end =" ")
        print("belongs to ", self.location, 'has sold', self.Qty, 'Kgs of ',self.crop ,'to FCI, for further details contact', self.mob)

# Obj = FoodCorpInd()
# Obj.sale()
# Obj.totalPrice()
# Obj.farmerDetails()


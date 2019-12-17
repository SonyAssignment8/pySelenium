class Myntra():
    Beauty=['lipstick','creams','powders','nailpaint']
    points=150
    total=500
    amount=total-points
    def product(self):
        self.product=input("enter product:")
        print("product name is:",self.product)
    def addToCart(self):
        print(self.product," added to cart")
        print("The total amount is:",self.total)
        print("Total amount After discount:",self.amount)
    def payment(self):
        print("do the payments by choosing any one 1.cod 2.dc_cc 3.net banking")
        mode=input("enter mode of payment:")
        if mode=='1':
            print("cash on delivery done")
            self.points+=100
        elif mode=='2':
            print("money credited by credit or debit card")
            self.points += 100
        else:
            print("money credited by net banking")
            self.points += 100

    def cancellation(self):
        print("cancellation")
    def Return(self):
        print("return the product")
        print("After return the money is refunded to points")
        print("your total amount refunded  is:",self.amount)
    def exchange(self):
        print("exchange the products")

m=Myntra()
m.product()
m.addToCart()
m.payment()
r=input("enter if u want to 1. cancel ,2.return 3. exchange 4.exit")
if r=='1':
 m.cancellation()
elif r=='2':
    m.Return()
elif r==3:
   m.exchange()
else:
    print("Thank you")
class Amazon():
    Men = 'mensection'
    women = 'Wonemsection'
    kids = 'kidssection'
    accessories = 'accessories'
    payment = 'payment'
    goods = 'goods'
    exchange = 'exchange goods'
    ret = 'Return'

    def men(self):
        sel = input("Please enter choice :"'\n'"1.cloths"'\n'"2.shoes"'\n'"3.other")
        print(sel)

    def women(self):
        sel = input("Please enter choice :"'\n'"1.cloths"'\n'"2.shoes"'\n'"3.other")
        print(sel)

    def kids(self):
        sel = input("Please enter choice :"'\n'"1.Toys"'\n'"2.games"'\n'"3.other")
        print(sel)

    def accessories(self):
        sel = input("Please enter choice :"'\n'"1.Ring"'\n'"2.Nailpaint"'\n'"3.other")
        print(sel)

    if input(1):
        print("You Select :"'\n'"1. Gold Ring"'\n Silver Ring')
    elif input(2):
        print("you selct nailpaint "'\n'"Blue color"'\n'" red color")
    elif input(3):
        print("Please select other option :")
    else:
        print("you enter wrong input")

    def goods(self):
        sel = input("Please enter choice :"'\n'"1.Electronics"'\n'"2.Furniture"'\n'"3.other")
        print(sel)

    def exchange(self):
        sel = input("Please enter choice :"'\n' "1.yes"'\n'"2.No")
        print(sel)

    def ret(self):
        sel = input("Please enter choice :"'\n' "1.yes"'\n'"2.No")
        print(sel)

    def payment(self):
        sel = input("Please select Payment mode"'\n'" 1.CCAvenue"'\n'" 2.Pay U")
        print(sel)

# a= Amazon()
# a.men()
# a.women()
# a.kids()
# a.accessories()
# a.goods()
# a.exchange()
# a.ret()
# a.payment()






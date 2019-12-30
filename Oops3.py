class Bank():
    Name = input("Enter Name:")
    ac_no= int(input("Enter account number"))
    mobile = int(input("Enter mobile number"))
    def deposit(self):
        print("Please deposit into",self.ac_no)
        self.deposit = int(input("enter amount:"))
    def details(self):
        print(self.Name,"bearing","A/C no",self.ac_no)
        print("The amount deposited is Rs",self.deposit)

b = Bank()
print(b.mobile)
b.deposit()
b.details()
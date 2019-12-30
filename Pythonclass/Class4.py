class Account():
    amount=2000
    deduction=0;
    def balance(self):
        bal=amount-deduction
    def withdraw(self):
        deduction=int(input("enter the deduction amount"))

a = Account()
a.withdraw()
print(bal)
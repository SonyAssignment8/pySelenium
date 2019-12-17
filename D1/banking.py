class Banking():
    print("Bank Details")
    adhar = input("Enter adhaar number:")
    AC_no = input("Enter account number")
    DC = int(input("Enter Debit card no:"))
    acc_type = input("Enter account type")

    balance = 0

    #Deposit
    def deposit(self):
        self.deposited_amnt = int(input("Enter the amount to deposit"))
        self.balance = self.deposited_amnt
        print("Total balance Rs:",self.balance)

    #Withdraw
    def withdraw(self):
        self.withdraw_amnt = int(input("Enter the amount to withdraw"))
        # if self.balance == 0:
        #     print("Insufficient Balance,Please deposit to withdraw")
        self.balance-=self.withdraw_amnt

        print("Amount withdrawn successfully of Rs:",self.withdraw_amnt)
        print("Total Balance Rs:",self.balance)
        print("--------------------------------")
        print("Thank you for banking with us")

# bank = Banking()
# bank.deposit()
# bank.withdraw()
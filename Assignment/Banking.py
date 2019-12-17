class Bank():
    name=input('Enter ur name')
    contact_no=int(input('Enter ur contact number'))
    adress=input('Enter ur address')
    balance=10000
    #transfer the amount
    def transfer(self):
        self.amount=int(input('Enter the amount to be transfered'))
        print('The amount transfered is:',self.amount)
     #check the balance
    def balance1(self):
        self.balance=self.balance-self.amount
        print(Bank.name)
        print(Bank.contact_no)
        print(Bank.adress)
        print('Your Balance is :',self.balance)
# b=Bank()
# b.transfer()
# b.balance1()
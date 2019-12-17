class Bank():
    Bank_name = "ICICI"
    L_ROI = 14
    MBL = "Bangalore"

    def __init__(self,name,age,phno,email,bal=0):
        self.name = name
        self.age = age
        self.phno = phno
        self.email = email
        self.bal = bal
    def deposit(self,amt = 0):
        if amt ==0:
            amt = self.get_amount()
        self.bal+=amt
        self.success()

    def withdraw(self,amt=0):
        if amt ==0:
            amt = self.get_amount()
        if amt>self.bal:
            self.failure()
            print("Insufficient Funds")
            return
        self.bal = self.sub(self.bal,amt)
        self.success()
    def display(self):
        print(self.name,self.age,self.email,self.bal)
    #object methods(called after creating object,user specific)
    def modify(self,name="",age=0,phno=0,email=""):
        if name!="":
            self.name = name
        if age!=0:
            self.age = age
        if phno!=0:
            self.phno = phno
        if email!="":
            self.email = email
        self.success()
    @classmethod
    def change_Bname(cls,new=""):
        if new =="":
            cls.Bank_Name = new
        cls.success()
    @classmethod
    def modify_ROI(cls,new=0):
        if new==0:
            new = cls.get_ROI()
            cls.ROI = new
            cls.success()
    @staticmethod
    def get_ROI():
        new = float(input("Enter new ROI"))
        return new
    @staticmethod
    def sub(a,b):
        return a-b
    @staticmethod
    def failure():
        print("Transaction failed")
    @staticmethod
    def get_amount():
        amount = int(input("Enter the amount"))
        return amount
    @staticmethod
    def success():
        print("Transaction successful'")
Reeta = Bank("Reeta",25,91232323,"reeta@bata.com",10000)
Bank.modify_ROI()
Reeta.display()
Reeta.withdraw(700)
Bank.display(Reeta)
Bank.withdraw(Reeta,1000)

class Bank2(Bank):
    def __int__(self,name,age,phno,email,Pan,aadhar,bal=0):
        super(Bank2,self).__init__(name,age,phno,email,bal=0)
        self.Pan=Pan
        self.aadhar = aadhar
    def add_aadhar_pan(self,Pan,aadhar):
        self.Pan=Pan
        self.aadhar = aadhar
    def display(self):
        print(self.name,self.age,self.phno,self.email,self.Pan,self.aadhar,self.bal)

Bank2.add_aadhar_pan(Reeta,"qwert4567",123456789)
print(Reeta.aadhar)
print(Reeta.Pan)
Bank2.display(Reeta)


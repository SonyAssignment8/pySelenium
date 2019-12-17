class Bank():
    Bank_name="ICICI"
    ROI=12
    MBL="Mumbai"
    def __init__(self,Name,Age,Phno,Email,Bal=0):
        self.Name=Name
        self.Age=Age
        self.Phno=Phno
        self.Email=Email
        self.Bal=Bal
    def deposit(self,amt):
        if amt==0:
            amt=self.get_amount()
            self.Bal+=amt
            self.success()
    def withdraw(self,amt=0):
        if amt==0:
            amt=self.get_amount()
        if amt>self.Bal:
            self.failure()
            print("Insufficient Funds")
            return
            self.Bal=self.sub(self.Bal,amount)
            self.success()
    def display(self):
         print(self.Name,self.Age,self.Phno,self.Email,self.Bal)
    def modify(self,Name="",Age=0,Phno=0,Email=""):
        if Name!="":
           self.Name=Name
        if Age!=0:
            self.Age=Age
        if Phno!=0:
            self.Phno=Phno
        if Email!="":
            self.Email=Email
        self.success()
    @classmethod
    def change_BName(cls,new=""):
        if new=="":
            cls.Bank_Name=new
            cls.success()
    @classmethod
    def modify_ROI(cls,new=0):
        if new==0:
            new=cls.get_ROI()
            cls.ROI=new
            cls.success()
    @staticmethod
    def get_ROI():
        new=float(input("Enter new ROI"))
        return new
    @staticmethod
    def sub(a,b):
        return a-b
    @staticmethod
    def failure():
        print("Transaction failure")
    @staticmethod
    def get_amount():
        amount=int(input("Enter the amount"))
        return amount
    @staticmethod
    def success():
        print("Transaction done successfully")
Reeta = Bank("Reeta", 92877799, "reeta@gamil.com", 1000)
seeta = Bank("sita", 9898787978, "sita@gmauil.com", 2000)
Bank.display(Reeta)
Reeta.withdraw(1000)
Reeta.withdraw()
Bank.display(Reeta)
Bank.withdraw(Reeta,1000)
Bank.modify_ROI()
Reeta.get_ROI()
print(Reeta.ROI)

class Bank1(Bank):
    def __init__(self, Name, Age, Phno, Email, Pan, Aadhar, Bal=0):
        super(Bank, self).__init__(Name, Age, Phno, Email, Bal=0)
        self.Pan = Pan
        self.Aadhar = Aadhar

    def add_adhar_pan(self, Pan, Aadhar):
        self.Pan = Pan
        self.Aadhar = Aadhar
    def display(self):
         print(self.Name,self.Age,self.Phno,self.Email,self.Bal,self.Pan,self.Aadhar)
Bank1.add_adhar_pan(Reeta,"NM909978677",7654321896)
print(Reeta.Aadhar)
print(Reeta.Pan)
Bank1.display(Reeta)







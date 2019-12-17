class Bank:
    Bank_name="HDFC"
    ROI=14
    MB='Mumbai'
    def __init__(self,Name,Age,Phno,Email,Bal=0):
        self.Name=Name
        self.Age=Age
        self.Phno=Phno
        self.Email=Email
        self.Bal=Bal
    def display(self):
        print(self.Name,self.Age,self.Phno,self.Email,self.Bal)
    def deposit(self,amt=0):
        if amt==0:
            amt=self.get_amount()
        self.Bal+=amt
        self.success()
    def withdraw(self,amt=0):
        if amt==0:
            amt=self.get_amount()
        if amt>self.Bal:
            self.failure()
            print("insufficient amount")
            return
        self.Bal=self.sub(self.Bal,amt)
        self.success()

    def modify(self,Name="",Age=0,Phno=0,Email="",Bal=0):
        if Name!="":
            self.Name=Name
        if Age!=0:
            self.Age=Age
        if Phno!=0:
            self.Phno=Phno
        if Email!="":
            self.Email=Email
        if Bal!=0:
            self.Bal=Bal
    @classmethod
    def change_BName(cls,new=""):
        if new=="" :
            cls.Bank_Name=new
        cls.success()
    @classmethod
    def modify_ROI(cls,new=0):
        if new==0:
            new=cls.get_ROI()
        cls.ROI=new
    @staticmethod
    def success():
        print("trancation successfull")
    @staticmethod
    def get_amount():
        amount=int(input("Enter a amount"))
        return amount
    @staticmethod
    def failure():
        print("transcation failure")
    @staticmethod
    def sub(a,b):
        return a-b
    @staticmethod
    def get_ROI():
        new=float(input("Enter new ROI"))
        return new
class Bank2(Bank):
    def __init__(self, Name, Age, Phno, Email,Pan,Aadhar, Bal=0):
        super(Bank2,self).__init__(Name, Age, Phno, Email, Bal=0)
        self.Pan = Pan
        self.Aadhar = Aadhar
    def add_pan_aadhar(self,Pan,Aadhar):
        self.Pan = Pan
        self.Aadhar = Aadhar
    def display(self):
        print(self.Name,self.Age,self.Phno,self.Email,self.Pan,self.Aadhar,self.Bal)

riya=Bank("riya",23,2908765416,"riya@gmail.com",20000)
riya.display()
sita=Bank("sita",23,2908765416,"sita@gmail.com",50000)
ram=Bank2("ram",29,34788,"rm@gnail.com","yhui788",90876,10000)
ram.display()
riya.withdraw()
riya.display()
Bank2.add_pan_aadhar(riya,'2lki34',908765)
print(riya.Pan)
print(riya.Aadhar)
Bank.withdraw(riya,1000)
riya.display()
Bank.modify_ROI()
print(riya.ROI)






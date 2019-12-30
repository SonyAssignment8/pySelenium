class Bank():
    bank_name="SBI"
    mbl="bangaluru"
    roi=8
    def __init__(self,name,acno,age,email,bal=0):
        self.name=name
        self.acno=acno
        self.age=age
        self.email=email
        self.bal=bal
    def modify(self,name="",age=0,phone=0,email=""):
        if name=="":
            self.name=name
        if age==0:
            self.age=age
        if phone==0:
            self.phnno=phone
        if email=="":
            self.email=email
        self.success()
    def display(self):
        print(self.name,self.acno,self.age,self.email,self.bal)
    def withdraw(self,amt):
        if amt==0:
            self.get_amount()
        if amt>self.bal:
            self.failure()
            return
        self.bal=self.sub(self.bal,amt)
        self.success()
    @staticmethod
    def sub(a,b):
        return a-b

    @staticmethod
    def success():
        print("transaction sucessfull.....")
    @staticmethod
    def get_amount(self):
        amount=int(input("enter the amount"))
        return amount
    @staticmethod
    def failure():
        print("Transaction declined")
    @classmethod
    def display_roi(cls,new):
        if new==0:
            new=cls.get_roi()
        cls.roi=new
        cls.success()
    @staticmethod
    def get_roi():
        new_roi=float(input("enter the new roi"))
        return new_roi
    @classmethod
    def modify_bank(cls,new):
        if new=="":
            new=cls.new_bank_name()
        cls.mbl=new
        cls.success()
    @staticmethod
    def new_bank_name():
        newbranch=input("enter the new main branchname")
        return newbranch



krishna=Bank("krishna",12221424,20,"shjahjash@gmial.com",20000)
krishna.display()
krishna.withdraw(1000)
krishna.display()
print(krishna.bal)
print(krishna.roi)
krishna.get_roi()
print(krishna.roi)







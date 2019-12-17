class Bank():
    Bank_Name = 'ICICI'
    ROI = 14
    MBL = 'Mumbai'

    def __init__(self, Name, Age, Phno, Email, Bal=0):
        self.Name = Name
        self.Age = Age
        self.Phno = Phno
        self.Email = Email
        self.Bal = Bal

    def deposit(self, amt=0):
        if amt == 0:
            amt = self.get_amount()
        self.Bal += amt
        self.success()

    def withdraw(self, amt=0):
        if amt == 0:
            amount = self.get_amount()
        if amt >= self.Bal:
            self.failure()
            print("insufficient funds")
            return
            self.Bal = self.sub(self.Bal, amt)
            self.success()

    def display(self):
        print(self.Name, self.Age, self.Phno, self.Email, self.Bal)

    def modify(self, Name="", Age=0, Phno=0, Email=""):
        if Name != "":
            self.Name = Name
        if Age != 0:
            self.Age = Age
        if Phno != 0:
            self.Phno = Phno
        if Email != "":
            self.Email = Email
        self.success()

    @classmethod
    def change_BName(cls, new=""):
        if new == "":
            cls.Bank_name = new
            cls.success()

    @classmethod
    def modify_ROI(cls, new=0):
        if new == 0:
            new.cls.get_ROI()
            cls.ROI = new
            cls.success()

    # static methods will be used to define generic actions which is common to all users
    @staticmethod
    def get_ROI():
        new = float(input("Enter new ROI:"))
        return new

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def failure():
        print("Transaction Failure")

    @staticmethod
    def get_amount():
        amount = int(input("Enter the amount:"))
        return amount

    @staticmethod
    def success():
        print("transaction successful")


class Bank2(Bank):
    def __init__(self, Name, Age, Phno, Email, Pan, Aadhar, Bal=0):
        super(Bank2, self).__init__(Name, Age, Phno, Email, Bal=0)
        self.Pan = Pan
        self.Aadhar = Aadhar

    def add_aadhar_pan(self, Pan, Aadhar):
        self.Pan = Pan
        self.Aadhar = Aadhar

    def display(self):
        print(self.Name, self.Age, self.Phno, self.Email, self.Pan, self.Aadhar, self.Bal)


Reeta = Bank("Reeta", 25, 890809809, "reeta@bata.com", 10000)
Seetha = Bank('Seetha', 26, 798696879, 'seetha@gmail.com')
Bank2.add_aadhar_pan(Reeta, "EZKPS135", 979863455)
print(Reeta.Aadhar)
print(Reeta.Pan)
Bank2.display(Reeta)
Bank.change_BName("SBI")
print(Bank.Bank_Name)
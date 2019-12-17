#Hospital Management
class Hospital():
    print("Hospital Management")
    print("--------------------")
    Patient_Name = input("Enter patient name:")
    Appointment_Id = int(input("Enter Appointment Id:"))
    Appointment_date = int(input("Enter Appointment date"))
    Doc_Namae = input("Enter Doctor's name:")

    print("----------------------------------")

    def Registration(self):
        print("Registration details are:")
        print("Patient Name:", self.Patient_Name,"Appointment Id:", self.Appointment_Id, "Appointment Date:",self.Appointment_date, "Doctor Name:", self.Doc_Namae)

    def Department(self):
        print("Welcome")
        self.dept_no = int(input("Select Department Number: 1.Radiology, 2.Cardiology, 3.Oncology::"))
        if self.dept_no==1:
            print("WElcome to Radiology")
        elif self.dept_no==2:
            print("Welcome to Cardiology")
        else:
            print("Welcome to Oncology")
    def Doc_Name(self):
        print("Doctor name:",self.Doc_Namae)
    def lab(self):
        print("Mr",self.Doc_Namae,"has referred you for the lab tests! Kindly contact the reception for more details")

    def pay(self):
        print("Please make the payment via cash/Card/Google pay/paytm")
    def insurance(self):
        print("Mr",self.Patient_Name,"you have choosen cash less insurance option")

h = Hospital()
h.Registration()
h.Department()
h.Doc_Name()
h.lab()
h.pay()
h.insurance()

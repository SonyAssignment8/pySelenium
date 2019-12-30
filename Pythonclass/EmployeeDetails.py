'''This Program is of storing employee details and salary details,
department details,leave letter,releaving letter'''
class Employee():
    empId="123456"
    client="tyss"
    location="bangaluru"
    salary=20000

    def employeedetails(self,empName):

        empn=empName=empName
        print("employee name",empn)
        print("Working for the client==>",e.client)
        print("Working in location==>",e.location)
        e.department()
        e.salarydetails()
    def department(self):
        print("department he works is:","Accounts")

    def salarydetails(self):
        sal=e.salary;
        print("emplyee salary:==>",sal)
        pf="889 Rs pm"
        print(pf)
        insur=1000
        print("insurane dducted per year",insur)
        hra=1500
        print("HRA for month",hra)
    def leave(self,reason):
        lev=reason
        print("how many days required for",lev,"leave")
        noofdays=int(input("enter number of days leave required"))
        if noofdays<=2:
            print("leave accepted for the requested",noofdays,"Days")

        else:
            print("salary will be deducted if u take more than two days")
            sal = e.salary / 30
            print("per day RS",sal,"will be deducted/day if u take more than two days")
    def relevingletter(self):
        print("Exit letter,3 months pay slips generated")

e=Employee()
data=int(input("1:-for employee details and 2:- for leave and 3:- for Releaving letter"))
if data==1:
    e.employeedetails(input("enter employee name"))
elif data==2:
    e.leave(input("enter reason for leave"))
elif data==3:
    e.relevingletter()



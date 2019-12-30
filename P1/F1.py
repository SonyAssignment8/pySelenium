from Pythonclass.EmployeeDetails import*
e=Employee()
data=int(input("1:-for employee details and 2:- for leave and 3:- for Releaving letter"))
if data==1:
    e.employeedetails(input("enter employee name"))
elif data==2:
    e.leave(input("enter reason for leave"))
elif data==3:
    e.relevingletter()




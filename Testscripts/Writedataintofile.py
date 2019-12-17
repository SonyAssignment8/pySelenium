#Write data in the excel file
from xlwt import Workbook
#workbook is created
wb=Workbook()
#add sheet is used to create sheet
sheet1=wb.add_sheet("Sheet1")
sheet1.write(0,0,"school")
sheet1.write(0,1,"office")
sheet1.write(0,2,"hospital")
wb.save("Book2.xls")
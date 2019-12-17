from xlwt import Workbook
#workbook is created
wb = Workbook()
#add sheet is used to create sheet
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(1,0,'ISBT Dehradun')
sheet1.write(2,0,'Mysore')
sheet1.write(3,0,'Nanjungud')
sheet1.write(4,0,'JBL Road')
sheet1.write(5,0,'Chamundi Vihar')
wb.save('Sample.xls')
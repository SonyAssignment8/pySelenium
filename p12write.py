from xlwt import Workbook

wb= Workbook()
sheet1 = wb.add_sheet('sheet 1')
sheet1.write(1,0,'bgm')
sheet1.write(2,0,'blr')
sheet1.write(3,0,'dk')
sheet1.write(4,0,'ch')
sheet1.write(5,0,'hyd')
sheet1.write(6,0,'klr')
sheet1.write(0,1,'name')
sheet1.write(0,2,'marks')
sheet1.write(0,3,'age')
sheet1.write(0,4,'add')
sheet1.write(0,5,'id')
sheet1.write(0,6,'phno')

wb.save("wSheet.xls")
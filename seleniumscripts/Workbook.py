import xlrd
loc="D:\sample.xls"
wb=xlrd.open_workbook(loc)
sheet1=wb.sheet_by_index(0)
rows=sheet1.nrows
cols=sheet1.ncols
for i in range(0,rows):
   for j in range(0,cols):
        print(sheet1.cell_value(i,j))

#write data into file
# from xlwt import Workbook
# wb=Workbook()
# sheet1=wb.add_sheet('sheet1')
# sheet1.write(1,0,'abc')
# sheet1.write(2,0,'hhgf')
# wb.save("D:\sample.xls")


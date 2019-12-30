#Read data from the excel sheet
import xlrd
loc="E:\Book1.xlsx"
wb=xlrd.open_workbook(loc)
#Get the first sheet by providing index
sheet1=wb.sheet_by_index(0)
#print the particular cell
print(sheet1.cell_value(0,1))
print(sheet1.ncols)
print(sheet1.nrows)
#Print all the data present in the sheet
Expname='qspider'
flag=False
for i in range(0,sheet1.nrows):
    names=sheet1.cell_value(i,0)
    print(names)
    if Expname == names:
        flag = True
#check if the particular data is present
assert flag,"False"
print("Expected name is found")

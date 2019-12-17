import xlrd

loc = 'D:\TestCase_Repository.xls'
wb = xlrd.open_workbook(loc)
sheet1 = wb.sheet_by_index(0)
print(sheet1.nrows)
print(sheet1.ncols)
# Checking 'Jyoti' is present in the list or not
name = 'jyoti'
flag = False
for i in range(0, sheet1.nrows):
    excelData = sheet1.cell_value(i, 1)
    if name in excelData:
        flag = True
        break
assert flag, print("name not found")
print("name found")



import xlrd

loc="D://example.xlsx"
wb=xlrd.open_workbook(loc)
sheet1=wb.sheet_by_index(0)
'''print(sheet1.cell_value(3,0))
print(sheet1.nrows)
print(sheet1.ncols)'''
#fetching all the data from excel sheet
n=sheet1.nrows
m=sheet1.ncols
for i in range(n):
    for j in range(m):
        print(sheet1.cell(i,j))

#fetching only row values
for i in range(0,n):
    print(sheet1.cell_value(i,0))

#fetching only columns values
for j in range(0,m):
    print(sheet1.cell_value(0,j))

import xlrd
loc="‪C:\sample.xlsx"
wb=xlrd.open_workbook(loc,'rb')
sheet1=wb.sheet_by_index(0)
# print(sheet1.ncols)
# print(sheet1.nrows)

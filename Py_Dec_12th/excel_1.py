from selenium import webdriver
import time
import xlrd
loc="C:/Users/Akshay/Desktop/excel_doc.xlsx"
wb = xlrd.open_workbook(loc)
sheet1 = wb.sheet_by_index(0)
#print(sheet1.cell_value(0,0))
#print(sheet1.cell_value(1,0))
#print(sheet1.cell_value(1,1))
rows=sheet1.nrows
col=sheet1.ncols
for i in range(rows):
    for j in range(col):
        print(sheet1.cell(i,j))
# sheet2 = wb.sheet_by_index(1)
# print(sheet2.cell_value(0,0))
# print(sheet2.cell_value(0,1))
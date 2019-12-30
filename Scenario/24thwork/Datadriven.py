#reading data from excel file
import openpyxl
excel_workbook=openpyxl.load_workbook("C:\\Users\\admin\\Desktop\\RTM.xlsx")
sheet=excel_workbook.get_sheet_by_name("Testcases")
print(sheet['E2'].value)
print(sheet.cell(row=2,column=4).value)

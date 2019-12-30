import openpyxl
wb=openpyxl.load_workbook("J:\\DataDriven.xlsx")
sheet=wb.get_sheet_by_name("Sheet1")
sheet['A2'].value=20               #remove ==20 if you want to fetch the data from excel
value=sheet.cell(row=5,column=5).value=40
wb.save("J:\\DataDriven.xlsx")

#dot properties file



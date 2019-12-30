#Write a data in excel sheet
import openpyxl
excel_workbook=openpyxl.load_workbook("C:\\Users\\admin\\Desktop\\RTM.xlsx")
excel_workbook.create_sheet("Sample",3)
sheet=excel_workbook.get_sheet_by_name("Sample")
sheet['A2'].value=20
excel_workbook.save("C:\\Users\\admin\\Desktop\\RTM.xlsx")


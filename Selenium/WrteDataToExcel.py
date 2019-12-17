from xlwt import Workbook
wb = Workbook()
# Add sheet is used to create sheet
sheet1 = wb.add_sheet("Sheet 1")
sheet1.write(1,0, "uyeuiyi")
sheet1.write(2,0,"uiooiip")
sheet1.write(3,0,"hiouoi")
sheet1.write(4,0,"yiuoyu")
sheet1.write(5,0,"yuiyiuyiuio")

# Saving file in particular given location
wb.save("D:\sample.xls")

# Saving file in the project folder itself
wb.save("sample.xls")

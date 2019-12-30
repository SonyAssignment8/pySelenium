from xlwt import Workbook
wb = Workbook()
sheet1 = wb.add_sheet('sheet 1')          # import objet of workbook and cqall
sheet1.write(1, 0, 'abhi raaj')           # use this command to write
sheet1.write(2, 0, 'ram raheem')
sheet1.write(3, 0, 'ramesh raaj')
sheet1.write(4, 0, 'ravan raaj')
sheet1.write(5, 0, 'uppar raaj')
sheet1.write(6, 0, 'lower raaj')

wb.save("D:/test1.xls")                  # Saivng fie in given path



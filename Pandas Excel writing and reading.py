import pandas as pd
dt = pd.DataFrame({
    'Slno':['1','2','3','4'],
    'Name':['Rashmi','Divya','Revanna','Jyothi'],
    'Address':['Bang','Mys','Delhi','mang']
})
print(dt)
writer = pd.ExcelWriter('E:\\test1.xlsx',engine='xlsxwriter')
dt.to_excel(writer,'sheet1')
writer.save()
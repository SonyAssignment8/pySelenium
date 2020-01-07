#Fetch program from excel
import pandas as pd
dt=pd.DataFrame({'Sino':[1,2,3,4],
                 'Name':['Divya','Deepu','Ravi','Rithu'],
                 'Address':['Bangalore','Bangalore','Bangalore','Bangalore']
                 })
dt=dt[['Sino','Name','Address']]
print(dt)

#write data in excel
writer=pd.ExcelWriter('Sample.xlsx',engine="xlsxwriter")
dt.to_excel(writer,'Sheet1')
writer.save()

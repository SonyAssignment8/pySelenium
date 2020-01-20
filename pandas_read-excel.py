import pandas as pd
excel_data = pd.read_excel("E://test1.xlsx")
df = excel_data.set_index("Slno")
print(df)
print('_______')


print(excel_data.head(3))
print(excel_data.tail(1))

# df.loc[startrow:endrow,startcolumn:endcolumn]
print("to access only 2 rows and its details :", df.loc["1":'Rashmi','Name':'Address'])

#print('---------')
#a = df.loc('sql',:
#print("to ")
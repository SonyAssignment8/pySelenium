import pandas
excel_data=pandas.read_excel("Sample.xlsx")
df=excel_data.set_index('Sino')
print(df)
print(excel_data.head(2))
print(excel_data.tail(1))
print("To access only 2 rows and its details:",df.loc['2':'3','Name':'Address'])
a=df.loc['1':]
print(a)


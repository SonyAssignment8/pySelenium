dict1 = {'Tanvi':'SDET','Jyoti':'Python', 'Sujitha':'Python', 'Divya':'Python',
        'Supriya':'Javascript', 'Sasmita':'Javascript', 'Dhanshekar':'Appium',
        'Kadambari':'Appium','Piyush':'Appium','Shushma':'Appium'}

print('1.Python \n 2. Javascript \n 3.Appium \n 4.SDET')
select = int(input("Please select any one option"))
if(select == 1 and dict1.values()=='Python'):
        print()

elif(select == 2):
    print(javascript)
elif(select == 3):
    print(appium)
elif(select == 4):
    print(sdet)
else:
    print("enter a valid select number")




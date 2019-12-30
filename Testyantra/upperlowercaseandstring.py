# string = 'atulvish@123ISEnough!!'
string = input("Enter string:")
count1=0
count2=0
count3=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
      elif(i.isnumeric()):
            count3=count3+1
print("The number of lowercase characters are:")
print(count1)
print("The number of uppercase characters are:")
print(count2)
print("The number of numeric are :")
print(count3)

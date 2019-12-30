#question no 10) WAP tp get n-student informationlike age dept using nested dictionary

StudentDetails={"reg1":{"name":"kushal","Age":12,"department":"A-sec"},"reg2":{"name":"kushi","Age":14,"department":"B-sec"},
"reg3":{"name":"sammu","Age":8,"department":"A-sec"},"reg4":{"name":"manvitha","Age":6,"department":"B-sec"},
"reg5":{"name":"Lekhana","Age":8,"department":"A-sec"}}



#Add New Student information
new ={"reg6":{"name":"dhruva","Age":4,"department":"LKG"}}
StudentDetails.update(new)
print(StudentDetails)
#Search for a pertiular student
stdd=StudentDetails.get(input("Enter Register number"))
print(stdd)

# #Delete the perticular student information
# StudentDetails.__delitem__("reg1")
# print(StudentDetails)

#Update students age
print(StudentDetails)


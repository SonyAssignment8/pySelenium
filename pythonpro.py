# pythonname={"Sujitha":"python","Jyoti":"python","Divya":"python"}
# javascriptname={"Supriya":"javascript","Sajeena":"javascript"}
# sdetname={"Payal":"sdet","Jyoshna":"sdet"}
# print("1.Python")
# print("2.Javascript")
# print("3.SDET")
# course=int(input("Select Your course"))
# if course==1:
#     print(pythonname.keys())
# elif course==2:
#     print(javascriptname.keys())
# else:
#     print(sdetname.keys())


pythonname={"Sujitha","Jyoti","Divya"}
python=[]
javascriptname={"Supriya","Sajeena"}
java=[]
sdetname={"Payal","Jyoshna"}
sdet=[]
print("1.Python")
print("2.Javascript")
print("3.SDET")
course=int(input("Select Your course"))
if course==1:
    print(pythonname)
    python.append(pythonname)
elif course==2:
    print(javascriptname)
else:
    print(sdetname)
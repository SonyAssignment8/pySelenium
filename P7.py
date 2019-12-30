# 7.WAP to take a marks of 5 subjects of the student & display the grade
# 80-100 - A
# 70 - 80 - A+
# 60-70 - B+
# 40-50 -
eng =int(input("Enter the marks for english:"))
sci=int(input("Enter the marks for Science:"))
kan=int(input("Enter the marks for Kannada:"))
math=int(input("Enter the marks for Math:"))
music=int(input("Enter the marks for music:"))
avg = ((eng+sci+kan+math+music)/500)*100
print(avg)
if (avg>=80):
    print("Grade A+")
elif(avg>=70):
    print("Grade A")
elif(avg>=60):
    print("Grade B")
else:
    print("Grade C")

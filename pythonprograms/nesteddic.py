student={1:{'name':'arun','age':'20','dept':'cse','percentage':'72'},
         2:{'name':'varun','age':'21','dept':'e&c','percentage':'62'}
         }
#add new student
s3={'name':'davan','age':'21','dept':'e&c','percentage':'60'}
student.setdefault(3,s3)
print(student)

#search new student
print(student.get(2))

#delete student
print(student.pop(3))

#update student marks
student.update({2:{'name':'varun','age':'21','dept':'e&c','percentage':'90'}})
print(student)

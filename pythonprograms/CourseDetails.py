course={'ram':'Python','sam':'Python','dam':'Python','arun':'sdet','varum':'sdet','suman':'js'}
name=input("enter student name:")
print("the course is:",course.get(name))

cour=input("enter course:")
if cour=='Python':
    value=course.values()
    if value.__eq__("Python"):
        print(course.keys())
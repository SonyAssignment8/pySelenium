class Student():
    #Nested dictionary
    d= {1:{'name': 'Rithu', 'age': '27', 'dep': 'csc','percentage':'80'},
          2:{'name': 'Meena', 'age': '22', 'dep': 'IT','percentage':'90'}}
    print(d)
    #add new student information
    #d1={5:{'name':'Divya','age':'25','dep':'ECE','percentage':'95'}}
    d.setdefault(5,{'name':'Divya','age':'25','dep':'ECE','percentage':'95'})
    print(d)
    #search for a student using reg number
    print(d.get(3))
    #delete particular student information
    d.pop(2)
    print(d)
    #update the particular student marks
    d.update({2:{'name':'Deepu1','age':'25','dep':'ECE','percentage':'95'}})
    print(d)
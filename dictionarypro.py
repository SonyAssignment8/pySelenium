
#Directory
dec={1:{"name":"Sujitha","Age":"30","Department":"Python","Percentage":"50"},2:{"name":"divya","Age":"30","Department":"Python","Percentage":"50"},3:{"name":"Rashmi","Age":"30","Department":"Python","Percentage":"50"}}
print(dec.values())
#search
print(dec.get(1))
#Update
dec.update({4:{"name":"jyoti","Age":"30","Department":"Python","Percentage":"50"}})

dec.setdefault(5,{"name":"jyoti","Age":"30","Department":"Python","Percentage":"50"})
#Delete
dec.pop(1)
print(dec)









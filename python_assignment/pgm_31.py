# 32. Write a program to fetch json data.
import json

f=open("C:/Users/ankita/PycharmProjects/pgm/python_assignment/dict.json","r")
data=json.load(f)
print(data)
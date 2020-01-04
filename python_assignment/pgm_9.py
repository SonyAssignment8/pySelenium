# 9.How to handle JSON file in that file, how you fetch only keys

import json

f=open("C:/Users/ankita/PycharmProjects/pgm/python_assignment/dict.json","r")
data=json.load(f)
print(data.keys())
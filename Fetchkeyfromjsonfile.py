#.How to handle JSON file in that file, how you fetch only keys
import json
k=json.load(open("./demo.json",'r'))
for i in k:
    print(i)

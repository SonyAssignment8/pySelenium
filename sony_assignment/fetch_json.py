import json
# with open("C:\\Users\\rashmi\\python_selenium_advanced\\sony_assignment\\fj.json") as f:
#     dict=json.load(f)
#     k=dict.keys()
#     print( dict['k1'])
#     print(k)

#fetch json data
f2=open("fj.json",'r')
dict2=json.load(f2)
def getData(key):
    return dict2[key]
data=getData('k2')
print(data)

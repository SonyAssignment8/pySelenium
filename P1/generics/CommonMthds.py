import json
def getJsonData(fName,name,key):
    with open("./" + fName + ".json") as f:
        data = json.load(f)
    return data[name][key]

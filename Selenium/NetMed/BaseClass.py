# Import statements
import json
def getJsonProperty(key, value):
    jsnData = json.load(open(".\Data.json"))
    val = jsnData[key][value]
    return val
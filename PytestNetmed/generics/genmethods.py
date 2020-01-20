import json

def read_json_val(filename,name,key):
    json.load(open("C:\\Users\\user\\Desktop\\PytestNetmed\\PytestNetmed\\"+filename+".json"))
    return(data[name][key])
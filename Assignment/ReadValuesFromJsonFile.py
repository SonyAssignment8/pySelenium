import json
j_data=json.load(open("J:\PythonPrograms\Assignment\JsonFile.json"))
d=j_data["colour"]
print("keys in json file",d.keys())
print("values in json file",d.values())

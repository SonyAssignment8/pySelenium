import json
with open("C:\\Users\\rashmi\\python_selenium_advanced\\seleniumscripts\\j.json") as f:
 data=json.load(f)
 print(data["details"]["name"])
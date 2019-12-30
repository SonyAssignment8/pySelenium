from pyjavaproperties import Properties
p=Properties()
p.load(open("C:\\Users\\rashmi\\python_selenium_advanced\\seleniumscripts\\p.properties"))
print(p['name'],p['course'])

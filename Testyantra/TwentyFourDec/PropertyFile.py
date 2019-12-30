from pyjavaproperties import Properties
p = Properties()
p.load(open("D:\\Python\\atul.properties.py"))
print(p['Name'])


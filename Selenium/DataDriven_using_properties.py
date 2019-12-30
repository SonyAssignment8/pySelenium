from pyjavaproperties import Properties

p = Properties()
p.load(open("./test.properties"))
print(p['username'])
print(p)

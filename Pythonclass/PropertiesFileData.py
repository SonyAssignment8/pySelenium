#To fetch data from properties file
from pyjavaproperties import Properties
p=Properties()
p.load(open("./Pfile.properties"))
print(p['url'])
print(p["username"])
print((p["password"]))

#Read a data from properties file
from pyjavaproperties import Properties
p=Properties()
p.load(open("C:\\Users\\admin\\Desktop\\prop.properties"))
print(p['url'])

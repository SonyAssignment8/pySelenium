from pyjavaproperties import Properties
import json
class GetProperty():
    def getKey(self, key):
        p = Properties()
        p.load(open(".\Data.properties"))
        u=p[key]
        return u
    def getJsonProperty(self,value,key):
        data=json.load(open(".\Data.json"))
        u=data[value][key]
        return u


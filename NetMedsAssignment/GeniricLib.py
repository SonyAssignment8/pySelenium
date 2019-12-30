import json
class GetConfigdata():
    def data(self,key1,key2):
        data = json.load(open(".\commondata.json"))
        u = data[key1][key2]
        return u

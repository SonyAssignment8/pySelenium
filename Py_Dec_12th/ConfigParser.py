from configparser import ConfigParser, ExtendedInterpolation


c = ConfigParser()
c["settings"] = {
    'debug' : "true",
    'secret_key' : "abc123",
    'log_path' :  "E:\Python"
    }
c["DB"]={
    'db_name' : "Mysql",
    'db_type' : "RDBMS",
    'db_port' : 8888
    }

#with open ("E:\\Python\\sample.ini)

f = open("E:\Python\\sample1.ini","w")
c.write(f)
f.close()

#reading data from the config file

c = ConfigParser(interpolation = ExtendedInterpolation())
c . read("E:\Python\sample1.ini")
print(c.sections())
print(c.get("settings","secret_key"))
print(c.options("settings"))
print("DB" in c)
print(c.get('DB','db_port'))
print(c.getint('DB','db_default_port',fallback=3306))
print(c.getboolean("settings",'debug'))
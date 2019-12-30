# from configparser import ConfigParser
# c=ConfigParser()
# c["settings"]={'debug':'true',"secret_key":"abc12",'log_path':"J:\krishna"}
# c["DB"]={"db_name":"mysql","db_type":"RDBMS","db_port":8888}
# c["configue"]={"url":"https://www.localhost.8888","abc":"krishna"}
#
# f=open("J:\\sample.ini","w")
# c.write(f)
# print("created sucessfully...")
# f.close()

#how to read data from configuration file
from configparser import ConfigParser,ExtendedInterpolation
c=ConfigParser(interpolation=ExtendedInterpolation())
c.read("J:\sample.ini")
print(c.sections())
print(c.get("settings","secret_key"))
print(c.options("settings"))
print("DB" in c)
print(c.get("DB","db_port"))
print(c.getint("DB","db_default_port",fallback=3306))
print(c.getboolean("settings","debug"))
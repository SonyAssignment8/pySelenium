from configparser import ConfigParser, ExtendedInterpolation
# writing data in a config file
c = ConfigParser()
c["settings"] = {
    'debug': "true",
    'secret_key': "abc123",
    'log_path': "D:\\confffiiggg"
}
c["DB"] = {
    'db_name': "Mysql",
    'db_type': "RDBMS",
    'db_port': 8888
}
f = open("D:\\confffiiggg\\sample1.ini", "w")
c.write(f)
f.close()

# Reading data from a config file
c = ConfigParser(interpolation=ExtendedInterpolation())
c.read("D:\\confffiiggg\\sample1.ini")
print(c.sections())
print(c.get("settings",'secret_key'))
print(c.options("settings"))
print("DB" in c)
print(c.getint('DB','db_default_port',fallback=3306))
print(c.getboolean("settings",'debug'))


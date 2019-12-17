from configparser import ConfigParser,ExtendedInterpolation

c=ConfigParser(interpolation=\
                   ExtendedInterpolation())
c.read("D:\TestData\\sample1.ini")

#sections gives blocks in config file
print(c.sections())
print(c.get("settings",'secret_key'))

#options gives contains of the specified block
print(c.options("settings"))

print("DB" in c)
print(c.get('DB','db_port'))
print(c.getboolean("settings",'debug'))
print(c.getint('DB','db_default_port',fallback=4408))
from configparser import ConfigParser,ExtendedInterpolation
c=ConfigParser(interpolation=ExtendedInterpolation())
c.read("c:\\oar-flask\\sample.ini")
print(c.sections())
print(c.get('settings','secret_key'))
print(c.get('DB','db_port'))
print(c.getint('DB','db_default_port',fallback=3306))
from configparser import ConfigParser
c=ConfigParser()
c["settings"]={
    'debug':'true',
    'secret_key':'abc123',
    'log_path':'c:\\oar-flask'
}
c['DB']={
    'db_name':'mysql',
    'db_type':'RDBMS',
    'db_port':8888
}
f=open("c:\\oar-flask\\sample.ini",'w')
c.write(f)
f.close()
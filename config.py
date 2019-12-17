from configparser import ConfigParser
c=ConfigParser()
c["settings"]={
    'debug':"true",
    'secret_key':"abc123",
    'log_path':"D:\\TestData"
    }
c["DB"]={
    'db_name':"Mysql",
    'db_type':"RDMS",
    'db_port':8888
    }
c["Language"]={
    'l_name':"Mysql",
    'l_name1':"java",
    'l_name2':"python"
}
'''with open("D:\\TestData\\sample.ini","w") as f:
    c.write(f)'''
f=open("D:\\TestData\\sample1.ini","w")
c.write(f)
f.close()
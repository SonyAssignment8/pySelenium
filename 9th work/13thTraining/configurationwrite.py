from configparser import ConfigParser
c=ConfigParser()
c["Setting"]={'debug':'true','c1':'log'}
c["DB"]={'db_name':'mysql','c2':'port'}
fs=open('C:\\Users\\admin\\Desktop\\f.ini','w')
c.write(fs)
fs.close()
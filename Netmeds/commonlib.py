from selenium import webdriver
from pyjavaproperties import Properties
class commonlibrary:
    def choose_browser(browser):
        browser = input("enter browser")
        if browser=='chrome':
            driver=webdriver.Chrome()
            return driver
        elif browser=='firefox':
            driver=webdriver.Firefox()
            return driver
    def read_property(self,key):
        p1=Properties()
        p1.load(open("C:\\Users\\rashmi\\python_selenium_advanced\\Netmeds\\Netmeds.properties"))
        value= p1.getProperty(key)
        return value





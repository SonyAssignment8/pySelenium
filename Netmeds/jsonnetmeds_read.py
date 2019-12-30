import json
from selenium import webdriver
class GenericLib:
    def choose_browser(browser):
        browser = input("enter browser")
        if browser == 'chrome':
            driver = webdriver.Chrome()
            return driver
        elif browser == 'firefox':
            driver = webdriver.Firefox()
            return driver


    def read_property(self, key1,key2):
        with open("C:\\Users\\rashmi\\python_selenium_advanced\\Netmeds\\netmeds_json.json") as f:
            data=json.load(f)
            return data[key1][key2]

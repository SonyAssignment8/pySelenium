from Netmeds.commonlib import *
from selenium import webdriver
class Netmeds_1:

    def set_up(self):
        self.b = commonlibrary()
        self.driver =self.b.choose_browser()
        self.base_url =str(self.b.read_property('url'))
        self.login_id=self.b.read_property('login_id')
        print(self.base_url)
        print(self.login_id)
    def script_1(self):
        self.driver.implicitly_wait(3)
        self.driver.get(self.base_url)
        self.driver.find_element_by_id(self.login_id).click()
n=Netmeds_1()
n.set_up()
n.script_1()

# mobile_id=b.read_property()
# mobile_num=b.read_property()
# password_click=b.read_property()
# psw=b.read_property()
# password=b.read_property()
# driver.find_element_by_id(login_id).click()
# driver.find_element_by_id(mobile_id).send_keys(mobile_num)
# driver.find_element_by_xpath(password_click).click()
# driver.find_element_by_id(psw).send_keys(password)

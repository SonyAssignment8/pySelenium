from selenium.webdriver import ActionChains
import time
from selenium import webdriver

class Bluestones:
    def __init__(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Safari()

    def launchWebsite(self):
        self.driver.get("https://www.bluestone.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return

    def search(self):
        self.driver.find_element_by_xpath("//a[text()='10+1 Monthly Plan']").click()
        self.driver.find_element_by_name("amount").send_keys("5000")
        self.driver.find_element_by_id("Email").send_keys("ankita.m@testyantra.in")
        self.driver.find_element_by_id("gmsStart").click()
        self.driver.find_element_by_name("_eventId_savePersonalAddressDetails").click()

        act=self.driver.current_url
        print(act)
        exp="https://www.bluestone.com/goldmineOrder?execution=e2s1"
        assert act==exp,False
        True
        print("Error page")


b=Bluestones('chrome')
b.launchWebsite()
b.search()

from selenium.webdriver import ActionChains
import time
from selenium import webdriver

class Bluestones:
    def __init__(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Safari()

    def launchWebsite(self):
        self.driver.get("https://www.bluestone.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return

    def search(self):
        self.driver.find_element_by_xpath("//a[text()='10+1 Monthly Plan']").click()
        self.driver.find_element_by_name("amount").send_keys("5000")
        self.driver.find_element_by_id("Email").send_keys("ankita.m@testyantra.in")
        self.driver.find_element_by_id("gmsStart").click()
        self.driver.find_element_by_name("_eventId_savePersonalAddressDetails").click()

        act=self.driver.current_url
        print(act)
        exp="https://www.bluestone.com/goldmineOrder?execution=e2s1"
        assert act==exp,False
        True
        print("Error page")


b=Bluestones('chrome')
b.launchWebsite()
b.search()


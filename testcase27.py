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
        self.driver.find_element_by_id("gmsStart").click()
        act=self.driver.current_url
        assert act=="error message",False
        True


b=Bluestones('chrome')
b.launchWebsite()
b.search()


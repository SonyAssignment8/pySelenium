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
        self.driver.find_element_by_xpath("//div[@class='prcs-d c-link']").click()
        listOfCity=self.driver.find_elements_by_xpath("//ul[@class='side-bar']")
        print("Count of citys:",listOfCity.__sizeof__())
        for i in listOfCity:
            print(i.text)


b=Bluestones('chrome')
b.launchWebsite()
b.search()


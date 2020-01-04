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
        self.driver.find_element_by_name("search_query").send_keys("Rings")
        self.driver.find_element_by_name("submit_search").click()
        #self.driver.find_element_by_xpath("//span[text()='Below 15,000']").click()
        mousehover = self.driver.find_element_by_xpath("//span[text()='Price']")
        a = ActionChains(self.driver)
        a.move_to_element(mousehover).perform()
        self.driver.find_element_by_xpath("//span[text()='Rs.']").click()
        a=self.driver.find_element_by_xpath("//span[text()='16 Designs']").text
        print(a)


b=Bluestones('chrome')
b.launchWebsite()
b.search()


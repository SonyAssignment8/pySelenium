'''
Scenario 27
1. open browser
2. enter URL(bluestone)
3. click on goldmine 10+1 Scheme
4. with out entering monthly amount and email address and click on start now
5. verify whether error message is displaying or not .
6. Close browser.
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
class BlueStone:
    def __init__(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Safari()

    def launchWebsite(self):
        self.driver.get("https://www.bluestone.com/")
        time.sleep(5)
        self.monthlyplan()

    def monthlyplan(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Monthly Plan')]").click()
        self.driver.find_element_by_xpath("//input[@value='Start Now']").click()
        actual_text=self.driver.find_element_by_xpath("//li[text()='Amount is required']").text
        assert actual_text=="Amount is required","msg not displayed"
        print("error msg displayed")


b=BlueStone("chrome")
b.launchWebsite()
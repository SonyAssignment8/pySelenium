'''
Scenario 22
1. open Browser
2. enter URL(bluestone)
3. go to search and search for rings
4. move the cursor to Delivery time
5. get the count of Next Day Delivery
6. close browser
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

from selenium.webdriver.common.keys import Keys


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
        time.sleep(3)
        self.searchrings()
    def searchrings(self):
        self.driver.find_element_by_id("search_query_top_elastic_search").send_keys("rings",Keys.ENTER)
        element=self.driver.find_element_by_xpath("//a[text()='Next Day Delivery ']")
        ActionChains(self.driver).click_and_hold(element).perform()
        # self.driver.find_element_by_xpath("//div[@id='top-filter']//span[contains(text(),'Delivery Time')]").click()
        next_day_delivery=self.driver.find_element_by_xpath("//span[text()='Next Day Delivery (1400+ designs)']").text
        print(next_day_delivery)


b=BlueStone("chrome")
b.launchWebsite()
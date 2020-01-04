# Scenario 12
# 1. Open browser
# 2. Enter URL(bluestone)
# 3. click on offers
# 4. Select 75% off Making charge and click on it
# 5. Verify the products list display with 75% charging
# 6. close Browser
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
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return

    def offers(self):
        ring_we = self.driver.find_element_by_xpath("//a[@title='Offers']")
        act = ActionChains(self.driver)
        act.click_and_hold(ring_we).perform()
        self.driver.find_element_by_xpath("//span[contains(text(),'20% off on making charge')]").click()
        info_lst = self.driver.find_element_by_xpath("//span[@class='product-details']")
        print("Product name:", info_lst.get_attribute("data-details"))
        self.driver.close()
        return



b=BlueStone('chrome')
b.launchWebsite()
b.offers()

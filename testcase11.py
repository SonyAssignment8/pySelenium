'''Scenario 11
1. Open browser
2. Enter URL(bluestone)
3. click on offers
4. Select 0% off Making charge and click on it
5. Verify the products list display with 0% charging
6. close Browser'''
from selenium import webdriver
from selenium.webdriver import ActionChains


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

    def coins(self):
        ActionChains(self.driver).




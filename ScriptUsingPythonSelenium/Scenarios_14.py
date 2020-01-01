'''Scenario 14
1. Open browser
2. Enter URL(bluestone)
3. move to Gold coins
4. Select 1 Gm
5. Verify 1Gm Coin is displaying or not
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
        coins_link=self.driver.find_element_by_xpath("//a[text()='Coins ']")
        ActionChains(self.driver).move_to_element(coins_link).perform()

b=BlueStone("chrome")
b.launchWebsite()
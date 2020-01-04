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

    def coins(self):
        mousehover = self.driver.find_element_by_xpath("//a[text()='Coins ']")
        a = ActionChains(self.driver)
        a.move_to_element(mousehover).perform()
        lst_coins = self.driver.find_elements_by_xpath(
            "//span[@data-p='all-jewellery-goldcoins-lakshmi,m']/../..//span[contains(text(),'gram')]")
        actuallst = []
        for i in lst_coins:
            data = i.text
            actuallst.append(data)
        print(actuallst)
        assert "50 gram" in actuallst, "Coin is not in the list"
        print("50 gram coin present in the list")
        return

b=BlueStone('chrome')
b.launchWebsite()
b.coins()
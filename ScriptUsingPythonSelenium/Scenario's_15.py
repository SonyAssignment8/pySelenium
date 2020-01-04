'''
Scenario 15
1. Open browser
2. Enter URL(bluestone)
3. move to Gold coins
4. Go to plain gold coins and Select 2 Gm
5. Verify 2Gm Coin is displaying or not.
6. close Browser
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
        self.getcoins()
    def getcoins(self):
        self.driver.maximize_window()
        ring_we=self.driver.find_element_by_xpath("//a[@title='Coins']")
        ActionChains(self.driver).move_to_element(ring_we).perform()
        lst_coins=self.driver.find_elements_by_xpath("//span[text()='Plain Gold Coins']/../following-sibling::ul/li/span[text()='2 gram']")
        actuallst=[]
        for i in lst_coins:
            data=i.text
            actuallst.append(data)
        assert "2 gram" in actuallst,"Coin is not in the list"
        print("2 gram coin present in the list")
        self.driver.close()

b=BlueStone("chrome")
b.launchWebsite()
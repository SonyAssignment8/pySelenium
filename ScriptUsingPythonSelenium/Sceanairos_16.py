'''
Scenario 14
1. Open browser
2. Enter URL(bluestone)
3. move to Gold coins
4. Select 1 Gm
5. Verify 1Gm Coin is displaying or not
6. close Browser
'''
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
        self.getcoins()
    def getcoins(self):
        ring_we=self.driver.find_element_by_xpath("//a[@title='Coins']")
        ActionChains(self.driver).move_to_element(ring_we).perform()
        lst_coins=self.driver.find_elements_by_xpath("//span[@data-p='all-jewellery-goldcoins-lakshmi,m']/../..//span[contains(text(),'gram')]")
        actuallst=[]
        for i in lst_coins:
            data=i.text
            actuallst.append(data)
        print(actuallst)
        assert "1 gram" in actuallst,"Coin is not in the list"
        print("1 gram coin present in the list")
        self.driver.close()

b=BlueStone("chrome")
b.launchWebsite()
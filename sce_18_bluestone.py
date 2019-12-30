'''
Scenario  16
1. Open browser
2. Enter URL(bluestone)
3. move to Gold coins
4. Go to plain gold coins and Select 20 Gm
5. Verify 20Gm Coin is displaying or not
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.bluestone.com/")
import time
time.sleep(3)
ring_we=driver.find_element_by_xpath("//a[@title='Coins']")
act=ActionChains(driver)
act.click_and_hold(ring_we).perform()
lst_coins=driver.find_elements_by_xpath("//span[@data-p='all-jewellery-goldcoins-lakshmi,m']/../..//span[contains(text(),'gram')]")
actuallst=[]
for i in lst_coins:
    data=i.text
    actuallst.append(data)
print(actuallst)
assert "20 gram" in actuallst,"Coin is not in the list"
print("20 gram coin present in the list")
driver.close()
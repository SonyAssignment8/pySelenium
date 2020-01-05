from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome(executable_path='C:\\Users\\kodiak\\Downloads\\chromedriver.exe')
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
assert "5 gram" in actuallst,"Coin is not in the list"
print("5 gram coin present in the list")
driver.close()
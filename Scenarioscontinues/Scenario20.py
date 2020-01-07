'''Scenario 19
1. Open browser
2. Enter URL(bluestone)
3. move to Gold coin
4. Go to Lakshmi gold coins and Select 10 Gm
5. Verify 5Gm Coin is displaying or not.
6. close Browser '''
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome("./chromedriver.exe")
#Navigate to bluestone page
driver.get("https://www.bluestone.com/")
driver.maximize_window()
action=ActionChains(driver)
element=driver.find_element_by_xpath("//a[@title='Coins']")
element_gram=driver.find_element_by_xpath("//span[text()='Lakshmi Gold Coins']/../..//ul/li/span[text()='10 gram']")

action.move_to_element(element).click(element_gram).perform()
time.sleep(4)
act=driver.find_element_by_xpath("//h1[text()='10 gram 24 KT Lakshmi Gold Coin']")
actual=act.text
exp='10 gram'
assert actual.__contains__(exp),'False'
print("Verification done-------->Pass")
driver.close()
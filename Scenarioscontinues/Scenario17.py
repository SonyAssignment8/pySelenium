'''Scenario 17
1. Open browser
2. Enter URL(bluestone)
3. move to Gold coins
4. Go to plain gold coins and Select 50 Gm
5. Verify 50 Gm Coin is displaying or not.
'''
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome("./chromedriver.exe")
#Navigate to bluestone page
driver.get("https://www.bluestone.com/")
driver.maximize_window()
action=ActionChains(driver)
element=driver.find_element_by_xpath("//a[text()='Coins ']")
element_gram=driver.find_element_by_xpath("//span[text()='50 gram']")
action.move_to_element(element).click(element_gram).perform()
time.sleep(4)
act=driver.find_element_by_xpath("//h1[text()='50 gram 24 KT Gold Coin']")
actual=act.text
exp='50 gram'
assert actual.__contains__(exp),'False'
print("Verification done-------->Pass")
driver.close()
'''
Scenario 11
1. Open browser
2. Enter URL(bluestone)
3. click on offers
4. Select 0% off Making charge and click on it
5. Verify the products list display with 0% charging
6. close Browser
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.bluestone.com/")
import time
time.sleep(3)
ring_we=driver.find_element_by_xpath("//a[@title='Offers']")
act=ActionChains(driver)
act.click_and_hold(ring_we).perform()
driver.find_element_by_xpath("//span[contains(text(),'20% off on making charge')]").click()
info_lst=driver.find_element_by_xpath("//span[@class='product-details']")
print("Product name-----------",info_lst.get_attribute("data-details"))
driver.close()
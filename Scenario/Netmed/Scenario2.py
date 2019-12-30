import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("./chromedriver.exe")
#Navigate to the page
driver.get("https://www.netmeds.com/")
driver.implicitly_wait(10)
driver.maximize_window()
driver.switch_to_frame("webklipper-publisher-widget-container-notification-frame")
#Handle the popup
driver.find_element_by_xpath("//span[text()='No Thanks']").click()
driver.switch_to_default_content()
time.sleep(4)
#Navigate to medicines page
driver.find_element_by_xpath("//a[text()='Medicine']").click()
driver.find_element_by_xpath("//a[text()='D']").click()
driver.find_element_by_xpath("//a[contains(text(),'Diabetes')]").click()
driver.find_element_by_xpath("//a[contains(text(),'Glucobay 25mg Tablet')]").click()
drop=driver.find_element_by_xpath("//select[@name='qty']").click()
sel=Select(drop)
sel.select_by_value('4')
driver.find_element_by_xpath("//button[@title='ADD TO CART']").click()
#verification
Ext_text="Glucobay 25mg Tablet 10'S"
act_text=driver.find_element_by_xpath("//a[contains(text(),'Glucobay 25mg Tablet')]").text
assert Ext_text==act_text,"False"
print("Medicine is added to the cart---->Pass")
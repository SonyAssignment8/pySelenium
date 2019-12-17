from selenium import  webdriver
import time
#from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get("https://www.craftsvilla.com")
driver.implicitly_wait(3)
mouseover=driver.find_element_by_xpath("//a[text()='SAREES']")
action=ActionChains(driver)
time.sleep(3)
action.move_to_element(mouseover).perform()
time.sleep(3)
driver.find_element_by_xpath("//a[text()='Cotton Sarees']").click()

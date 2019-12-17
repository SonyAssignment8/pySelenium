from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome()
driver.get("https://www.craftsvilla.com/")
driver.implicitly_wait(12)
driver.maximize_window()
mousehover=driver.find_element_by_xpath("//a[text()='SAREES']")
a=ActionChains(driver)
a.move_to_element(mousehover).perform()
time.sleep(9)
driver.close()
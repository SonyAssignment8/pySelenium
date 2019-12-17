import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.craftsvilla.com/")
driver.maximize_window()
wb = driver.find_element_by_xpath("//a[text()='SAREES']")
act = ActionChains(driver)
act.move_to_element(wb).perform()
time.sleep(10)
driver.close()

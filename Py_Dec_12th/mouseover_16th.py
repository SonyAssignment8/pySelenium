from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.craftsvilla.com/")
driver.maximize_window()
driver.implicitly_wait(10)
mouseHover = driver.find_element_by_xpath("//a[text()='SAREES']")
action = ActionChains(driver)
action.move_to_element(mouseHover).perform()
time.sleep(9)
driver.close()
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.find_element_by_id("searchDropdownBox").click()
time.sleep(2)

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.netmeds.com/")
import time
time.sleep(5)
driver.maximize_window()
driver.find_element_by_partial_link_text("/customer")

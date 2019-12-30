from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path="D:\Python\chromedriver.exe")
driver.get("https://accounts.google.com/")
driver.maximize_window()
driver.find_element_by_name("identifier").send_keys("atul.v@testyantra.com")
driver.find_element_by_class_name("CwaK9").click()
driver.implicitly_wait(30)
driver.find_element_by_name("password").send_keys("Teamwork@1")
driver.find_element_by_xpath("//span[text()='Next']").click()
driver.implicitly_wait(20)
driver.close()
driver.get("https://www.google.com/")
driver.maximize_window()
# driver.find_element_by_id("//input[@id='fakebox-input']").send_keys("gmail")
driver.find_element_by_class_name("gb_g").click()

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//input[@id='btnLogin']").click()
time.sleep(5)
driver.find_element_by_xpath("//a[@id='welcome']").click()
time.sleep(2)
driver.find_element_by_link_text("Logout").click()
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://mail.google.com/mail/u/0/#inbox")
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath("//input[@id='identifierId']").send_keys("akshay.kodur")
time.sleep(10)
driver.find_element_by_xpath("//span[text()='Next']").click()
time.sleep(5)
driver.find_element_by_name("password").send_keys("Robinhood29!")
time.sleep(5)
driver.find_element_by_xpath("//span[text()='Next']").click()

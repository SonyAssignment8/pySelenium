from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")
driver.find_element_by_tag_name("//input[@id='username']").send_keys("admin")
driver.find_element_by_name("//input[@class='textField pwdfield']").send_keys("manager")
driver.find_elements_by_link_text("Login ").click()

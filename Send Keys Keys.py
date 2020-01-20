from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(10)
driver.find_element_by_id("txtUsername").send_keys("Admin")
username.send_keys(Keys.CONTRAL+'a')
username.send_keys(Keys.DELETE)
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").send_keys(Keys.ENTER)
driver.close()
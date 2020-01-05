from selenium import webdriver
from selenium.webdriver.common.keys import Keys
d=webdriver.Chrome()
d.get("http://opensource-demo.orangehrmlive.com/")
d.implicitly_wait(3)
# d.find_element_by_id("txtUsername").send_keys("Admin")
# d.find_element_by_id("txtPassword").send_keys("admin123")
# d.find_element_by_id("btnLogin").send_keys(Keys.ENTER)
d.find_element_by_id("txtUsername").send_keys("Admin",Keys.TAB,"admin123",Keys.ENTER)
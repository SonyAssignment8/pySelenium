#Use of keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("./chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(10)
username=driver.find_element_by_id("txtUsername")
username.send_keys("Admin")
username.send_keys(Keys.CONTROL+'a')
username.send_keys(Keys.DELETE)

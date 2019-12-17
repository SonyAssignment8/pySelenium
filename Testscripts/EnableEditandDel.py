#Select option from create filter and check if edit and delete link is enabled
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("http://localhost:8888/")
#login to the application
driver.find_element_by_name("user_name").send_keys("admin")
driver.find_element_by_name("user_password").send_keys("manager")
driver.find_element_by_id("submitButton").click()
#Navigate to Organisation
driver.find_element_by_xpath("//a[text()='Organizations']").click()
#use Select class to select All option
sel=driver.find_element_by_xpath("//select[@id='viewname']")
a=Select(sel)
a.select_by_visible_text("NewFilter")
#Validate
Editbtn=driver.find_element_by_xpath("//span[text()='Edit']")
Deletebtn=driver.find_element_by_xpath("//span[text()='Delete']")
#Validate
assert Editbtn.is_enabled(),"False"
print("Verified------>pass")
assert Deletebtn.is_enabled(),"False"
print("Verified------>pass")
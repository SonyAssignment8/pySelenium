#Select All option from create filter and check if the Edit and Delete Options are disabled
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
a.select_by_visible_text("All")
Editbtn=driver.find_element_by_xpath("//span[text()='Edit']").is_enabled()
Deletebtn=driver.find_element_by_xpath("//span[text()='Delete']").is_enabled()
#Validate
assert Editbtn!='True',"False"
print("Verified------>pass")
assert Deletebtn!='True',"False"
print("Verified------>pass")
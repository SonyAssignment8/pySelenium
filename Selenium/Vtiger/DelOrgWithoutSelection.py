"""Trying to delete an Organization without
selecting any Organization"""

# Import statements
from selenium import webdriver

# Creating driver object
driver = webdriver.Chrome()

# Navigating to the URL
driver.get("http://localhost:8888/")

# Putting wait statement for page to load
driver.implicitly_wait(20)

# Login to the application
driver.find_element_by_xpath("//input[@name ='user_name']").send_keys("admin")
driver.find_element_by_xpath("//input[@name ='user_password']").send_keys("root")
driver.find_element_by_id("submitButton").click()

# Click on 'Organisations' link
driver.find_element_by_xpath("//a[text()='Organizations']").click()

# Click on delete button
driver.find_element_by_xpath("//input[@class='crmbutton small delete']").click()

# Verifying the alert message
exp_msg = 'Please select at least one entity'

# Switching to alert window and getting the text of it
act_msg = driver.switch_to.alert.text
assert exp_msg == act_msg, print("Message not verified as:", act_msg)
print("Message verified as:", act_msg)


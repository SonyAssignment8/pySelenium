"""Trying to delete an Organization by clicking
on respective checkbox and verifying the alert message """

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

# Try to delete an Organization by selecting respective checkbox
driver.find_element_by_xpath("//input[@name='selected_id']").click()

# Click on footer delete button
driver.find_element_by_xpath("//table[@class='lvtBg']//input[@class='crmbutton small delete'][1]").click()

# Switching to alert window and getting the text of it
act_msg = driver.switch_to.alert.text

# Verifying the alert message
exp_msg = 'Deleting this organization(s) will remove its related ' \
          'Opportunities & Quotes. Are you sure you want to delete the selected 1 records?'

assert exp_msg == act_msg,print("Message not verified as:", act_msg)
print("Message verified as:", act_msg)

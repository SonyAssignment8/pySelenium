"""Trying to select all the checkboxes by clicking one checkbox"""

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

# Click on select all checkbox
driver.find_element_by_xpath("//input[@id='selectCurrentPageRec']").click()
wb = driver.find_elements_by_xpath("//input[@name='selected_id']")

# Verifying all the checkbox is getting selected or not
for i in wb:
    assert i.is_selected(), print("Not selected")
    print("Checked")

# Close driver object
driver.close()
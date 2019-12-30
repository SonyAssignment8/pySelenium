"""Trying to delete an Organization by clicking on respective checkbox and
 verifying the organization name is present in recycle bin or not """

# Import statements
from selenium import webdriver

# Creating driver object
from selenium.webdriver import ActionChains

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

# Click on organization to  delete
count = 0
while count <= 10:
    try:
        wb = driver.find_element_by_xpath(
            "//tr[@class='lvtColData']//a[text()='Ispiders']/../..//a[text()='del']").click()
        count += 1
        break
    except:
        print("Exception Handled")

# Switch to alert window and accept it
driver.switch_to.alert.accept()

# Move to 'More' Dropdown and click on 'Recycle Bin'
while count <= 10:
    try:
        driver.find_element_by_xpath("//a[text()='More']").click()
        driver.find_element_by_xpath("//a[@name='Recycle Bin']").click()
        count += 1
        break
    except:
        print("Exception Handled")

# Getting the organization which is deleted
import time

time.sleep(5)
del_org_Name = driver.find_element_by_xpath("//table[@class='lvt small']/tbody/tr/td/a[text()='Ispiders']")
print(del_org_Name.text)

# Getting all the Organizations present in Org page
count = 0
while count <= 10:
    try:
        org_names = driver.find_elements_by_xpath("//tr[@class='lvtColData']/td[3]")
        break
    except:
        count + 1

# Validating the deleted organization name
for i in org_names:
    assert i.text == del_org_Name, print("Deleted organization is not present in Recycle bin")
    print("Deleted organization is not present in Recycle bin")

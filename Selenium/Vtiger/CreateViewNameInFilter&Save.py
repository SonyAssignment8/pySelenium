# Import statements
from selenium import webdriver

# Creating driver object
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

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

# Click on 'Create Filter' link
driver.find_element_by_xpath("//a[text()='Create Filter']").click()

# Creating a new filter
fil_name = "Member Of"
driver.find_element_by_xpath("//input[@name='viewName']").send_keys(fil_name)
driver.find_element_by_xpath("//input[@title='Save [Alt+S]']").click()

# Getting all the filter options and checking the new filter is present in the dropdown or not
sel = driver.find_element_by_id("viewname")
fil = Select(sel)
flag = False
for i in fil.options:
    if fil_name == i.text:
        flag = True
assert flag, print("New filter ",fil_name,"created is not present in the filter dropdown")
print("New filter created is present in the filter dropdown")

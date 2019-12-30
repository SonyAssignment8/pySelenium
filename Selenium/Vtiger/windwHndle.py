""" Window Handling """

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

# Click on 'Opportunities' link
driver.find_element_by_xpath("//a[text()='Opportunities']").click()

# Click on Plus(+) to  create an Opportunity
driver.find_element_by_xpath("//img[@title='Create Opportunity...']").click()

# Enter Opportunity name
driver.find_element_by_xpath("//input[@name='potentialname']").send_keys("JyotiSahu")
driver.find_element_by_xpath("//img[@src='themes/softed/images/select.gif']").click()

# Getting current window or parent window
curr_win = driver.current_window_handle

# Getting new opened window or child window
new_win = driver.window_handles[1]

# switch to child window
driver.switch_to.window(new_win)

# select org name
driver.find_element_by_xpath("//a[text()='Jspiders']").click()

# Switch back to old or parent window
driver.switch_to.window(curr_win)

# save the created opportunity
driver.find_element_by_xpath("//input[@title='Save [Alt+S]']").click()

# Close the driver object
driver.close()
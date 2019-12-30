
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import time

driver =webdriver.Chrome()
# privideing implicitly wait
driver.implicitly_wait(20)
# launch the browser

driver.get("http://localhost:8888/")
# Enter the manditory details and login to the application
driver.find_element_by_name("user_name").send_keys("admin")
driver.find_element_by_name("user_password").send_keys("manager")
driver.find_element_by_id("submitButton").click()

# click on organisation link
driver.find_element_by_xpath("//a[text()='Organizations']").click()

# click on filter link and create a filter by name krishna
driver.find_element_by_xpath("//a[text()='Create Filter']").click()
driver.find_element_by_xpath("//input[@title='Save [Alt+S]']").click()
#verify the popup message
expected="Missing required"
alt= driver.switch_to.alert
actual=alt.text
alt.accept()
if actual.__contains__(expected):
    print("TC PASS")
else:
    print("TC FAIL")
act = ActionChains(driver)
act.move_to_element(driver.find_element_by_xpath("//table/tbody/tr/td[2]/img")).perform()
driver.find_element_by_xpath("//a[text()='Sign Out']").click()
driver.close()
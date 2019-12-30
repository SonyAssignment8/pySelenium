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

# pre-condition  click on filter link and create a filter by name xyz
driver.find_element_by_xpath("//a[text()='Create Filter']").click()
driver.find_element_by_name("viewName").send_keys("xyz")
driver.find_element_by_xpath("//input[@title='Save [Alt+S]']").click()

# click on filtes drop down and select customised drop down krishna
drpdwn =driver.find_element_by_id("viewname")
sel =Select(drpdwn)
sel.select_by_visible_text("xyz")
# click on delete button
driver.find_element_by_xpath("//a[text()='Delete']").click()
#handel alert pop up
driver.switch_to.alert.accept()
# modify the name and save the new filter name
dd = driver.find_element_by_name("viewname")
time.sleep(5)
sel = Select(dd)
lst = sel.options
flag=False
for i in lst:
    if i.text=="xyz":
        flag=True
        break
    else:
        flag=False
if flag==False:
    print("TC PASS")
else:
    print("TC FAIL")

act=ActionChains(driver)
act.move_to_element(driver.find_element_by_xpath("//table/tbody/tr/td[2]/img")).perform()
driver.find_element_by_xpath("//a[text()='Sign Out']").click()
driver.close()

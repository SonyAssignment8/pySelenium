
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
driver.find_element_by_name("viewName").send_keys("krishna")
driver.find_element_by_xpath("//input[@title='Save [Alt+S]']").click()

# click on filtes drop down and select customised drop down krishna
drpdwn =driver.find_element_by_id("viewname")
sel =Select(drpdwn)
sel.select_by_visible_text("krishna")
# click on edit button
driver.find_element_by_xpath("//a[text()='Edit']").click()
# modify the name and save the new filter name
fltrName = driver.find_element_by_name("viewName")
fltrName.clear()
fltrName.send_keys("krishnakumar")
driver.find_element_by_xpath("//input[@title='Save [Alt+S]']").click()

dd = driver.find_element_by_name("viewname")
time.sleep(5)
sel = Select(dd)
lst = sel.options
flag=False
for i in lst:
    if i.text=="krishnakumar":
        flag=True
        break
    else:
        flag=False
if flag==True:
    print("TC PASS")
else:
    print("TC FAIL")

act=ActionChains(driver)
act.move_to_element(driver.find_element_by_xpath("//table/tbody/tr/td[2]/img")).perform()
driver.find_element_by_xpath("//a[text()='Sign Out']").click()
driver.close()

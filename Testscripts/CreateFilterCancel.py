#Create New Filter and cancel and check if the organisation page is displayed
import time
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
#Create new Filter
driver.find_element_by_xpath(("//a[text()='Create Filter']")).click()
driver.find_element_by_xpath("//input[@class='detailedViewTextBox']").send_keys("NewFilter")
time.sleep(4)
#use select
sel1=driver.find_element_by_xpath("//select[@name='column1']")
a=Select(sel1)
a.select_by_value("vtiger_account:accountname:accountname:Accounts_Account_Name:V")
sel2=driver.find_element_by_xpath("//select[@name='column2']")
b=Select(sel2)
b.select_by_value("vtiger_account:account_no:account_no:Accounts_Account_No:V")
sel3=driver.find_element_by_xpath("//select[@name='column2']")
c=Select(sel3)
c.select_by_value("vtiger_account:website:website:Accounts_Website:V")
driver.find_element_by_xpath("//input[@value='Cancel']").click()
#validate
Actresult=driver.find_element_by_xpath("//a[text()='Organizations']").text
print(Actresult)
Expresult='ORGANIZATIONS'
assert Expresult==Actresult, "False"
print("Validation Done ----->Pass")
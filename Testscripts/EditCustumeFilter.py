#Edit the create Filter and check if the filter is updated
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
b.select_by_value("vtiger_account:phone:phone:Accounts_Phone:V")
sel3=driver.find_element_by_xpath("//select[@name='column3']")
c=Select(sel3)
c.select_by_value("vtiger_account:fax:fax:Accounts_Fax:V")
driver.find_element_by_xpath("//input[@class='crmbutton small save']").click()
OrganisationName=driver.find_element_by_xpath("//td[@class='lvtCol']/a[text()='Organization Name']")
Phone=driver.find_element_by_xpath("//td[@class='lvtCol']/a[text()='Phone']")
Fax=driver.find_element_by_xpath("//td[@class='lvtCol']/a[text()='Fax']")
ExpOrgName="Organization Name"
ExpPhone="Phone"
ExpFax="Fax"
#Validate
assert ExpOrgName==OrganisationName.text,"False"
print("Verified-------->Pass")
assert ExpPhone==Phone.text,"False"
print("Verified-------->Pass")
assert ExpFax==Fax.text,"False"
print("Verified-------->Pass")
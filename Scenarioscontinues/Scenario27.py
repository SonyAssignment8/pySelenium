'''Scenario 27
1. open browser
2. enter URL(bluestone)
3. click on goldmine 10+1 Scheme
4. with out entering  monthly amount and email address and click on start now
5. verify whether error message is displaying or not .
6. Close browser.
'''
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome("./chromedriver.exe")
#Navigate to bluestone page
driver.get("https://www.bluestone.com/")
driver.maximize_window()
#Navigate to the goldmine 10+1 scheme
driver.find_element_by_xpath("//a[text()='10+1 Monthly Plan']").click()
#Click on start button without entering the fields
driver.find_element_by_xpath("//input[@id='gmsStart']").click()
#Get the failure message
act_amount=driver.find_element_by_xpath("//ul[@id='amount_error']").text
act_email=driver.find_element_by_xpath("//ul[@id='Email_error']").text
exp_amount="Amount is required"
exp_email="Email is required"
#Validation
assert act_amount==exp_amount and act_email==exp_email,"False"
print("The error message is displayed--->Pass")
driver.close()

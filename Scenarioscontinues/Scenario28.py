'''Scenario 28
1. open browser
2. enter URL(blustone)
3. click on goldmine 10+1 Sceheme
4. enter  monthly amount and email address and click on start now
5. verify wheather monthly amount and email address entered is reflected in this page
6. close browser'''
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome("./chromedriver.exe")
#Navigate to bluestone page
driver.get("https://www.bluestone.com/")
driver.maximize_window()
#Navigate to the goldmine 10+1 scheme
driver.find_element_by_xpath("//a[text()='10+1 Monthly Plan']").click()
#Click on start button by entering the fields
amount=driver.find_element_by_xpath("//input[@id='amount']").send_keys("1000")
email=driver.find_element_by_xpath("//input[@id='Email']").send_keys("deepu@aaa.com")
driver.find_element_by_xpath("//input[@id='gmsStart']").click()
exp_amount="Rs. 1,000"
exp_email="deepu@aaa.com"
act_email=driver.find_element_by_name("subscriptionAmount").text
amount=driver.find_element_by_id("email")
act_amount=amount.get_attribute("value")
print(act_amount)
print(act_email)
#validation
assert act_email==exp_email and act_amount==exp_amount,"False"
print("The verification is done ---->Pass")



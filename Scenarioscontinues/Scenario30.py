'''Scenario 30
1. open browser
2. enter URL(blustone)
3. click on goldmine 10+1 Sceheme
4. enter  monthly amount and email address and click on start now
5. with out filling any information click on next
6. verify wheather error msg is diaplaying or not in all fields
7. close browser Scenario '''
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
driver.find_element_by_xpath("//input[@type='submit']").click()
exp_contact=driver.find_element_by_xpath("//input[@id='contactNumber']").get_attribute("title")
exp_name=driver.find_element_by_xpath("//ul[@id='fullname_error']").text
exp_address=driver.find_element_by_xpath("//ul[@id='address_error']").text
exp_pincode=driver.find_element_by_xpath("//ul[@id='postcode_delivery_error']").text
act_contact="Please enter valid mobile number"
act_name="Name is required"
act_address="Your address is required"
act_pincode="Enter Valid Pincode"
assert exp_contact==act_contact and exp_address==act_address and exp_name==act_name and exp_pincode==act_pincode,"False"
print("failure message is verified ------>Pass")



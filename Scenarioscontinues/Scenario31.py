'''Scenario 31
1. open browser
2. enter URL(blustone)
3. click on goldmine 10+1 Sceheme
4. enter  monthly amount and email address and click on start now
5. fill  necessary details and click on next
6. Fill necessary details in next page
7. verify weather it is navigating to payment page or not . '''
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
email=driver.find_element_by_xpath("//input[@id='Email']").send_keys("deepu@ccc.com")
driver.find_element_by_xpath("//input[@id='gmsStart']").click()

driver.find_element_by_id("contactNumber").send_keys("9880623789")
time.sleep(2)
#driver.find_element_by_xpath("//form[@id='address-form']").clear()
driver.find_element_by_id("fullname").send_keys("deepu")
driver.find_element_by_id("address").send_keys("bangalore")
driver.find_element_by_id("postcode_delivery").send_keys("560018")
driver.find_element_by_xpath("//input[@type='submit']").click()
#Navigate to the next page
driver.find_element_by_id("nomineeName").send_keys("Divya")
driver.find_element_by_xpath("//input[@type='submit']").click()
#Payment page
act_title=driver.title
exp_title="Gold Mine Payment Option | BlueStone.com"
assert act_title==exp_title,"False"
print("The payment page is displayed--->Pass")
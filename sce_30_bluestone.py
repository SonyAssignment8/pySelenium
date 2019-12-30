'''
Scenario 30
1. open browser
2. enter URL(blustone)
 3. click on goldmine 10+1 Sceheme
  4. enter  monthly amount and email address and click on start now
  5. with out filling any information click on next
   6. verify wheather error msg is diaplaying or not in all fields
    7. close browser
'''

from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.bluestone.com/")
driver.find_element_by_xpath("//li[@class='menuparent repb nav-goldmine-link']").click()
driver.find_element_by_id("amount").send_keys("1000")
driver.find_element_by_id("Email").send_keys("sujitha@gmail.com")
driver.find_element_by_id("amount").clear()
driver.find_element_by_id("Email").clear()
driver.find_element_by_id("gmsStart").click()
import time
time.sleep(2)
act_err_mesg=driver.find_element_by_xpath("//div[contains(@class,'form-group')]").text
expe_err_mesg="Amount is required"
act_err_mesg1=driver.find_element_by_xpath("//div[contains(@class,'fl-wrap error')]").text
epe_erro_mesg="Email is required"

assert act_err_mesg==expe_err_mesg,"Test case failed"
print("Error mesg displayed ====pass")
driver.close()



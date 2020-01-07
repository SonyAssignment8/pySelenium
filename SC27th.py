from builtins import print

from selenium import webdriver
import time
#1 Open browser
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
#2 Enter URL(bluestone)
driver.get("https://www.bluestone.com/")
driver.maximize_window()
driver.implicitly_wait(12)

#3 click on goldmine 10+1 Scheme
driver.find_element_by_xpath("//a[@title='Gold Mine 10+1 Monthly Plan']").click()
#Scroll Down to start now button
driver.execute_script("window.scrollTo(0,500)")
time.sleep(1)
#4 with out entering monthly amount and email address and click on start now
driver.find_element_by_xpath("//input[@id='gmsStart']").click()

#5 verify whether error message is displaying or not .Email_error
errormsg_amnt = driver.find_element_by_xpath("//ul[@id='amount_error']").text
errormsg_email = driver.find_element_by_xpath("//ul[@id='Email_error']").text
actualerror_amnt = "Amount is required"
actualerror_email = "Email is required"
if actualerror_amnt == errormsg_amnt and actualerror_email == errormsg_email:
    print("Error Message displayed successfully")
else:
    print("Error message not displayed")
print(errormsg_amnt)
print(errormsg_email)
driver.close()


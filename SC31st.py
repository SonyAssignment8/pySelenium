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


gold_mine_title = driver.title
print(gold_mine_title)
#4. enter monthly amount and email address and click on start now
driver.find_element_by_xpath("//input[@id='amount']").send_keys("10000")
driver.find_element_by_xpath("//input[@id='Email']").send_keys("abc@gmail.com")

#5 with out entering monthly amount and email address and click on start now
driver.find_element_by_xpath("//input[@id='gmsStart']").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@name='_eventId_savePersonalAddressDetails']").click()

#6 Fill necessary details in next page
driver.find_element_by_xpath("//input[@name='_eventId_checkoutSaveAddressDetails']").click()

#7 Check if in payment page
payment_title = "Payment"
actual_payment_title = driver.find_element_by_xpath("//span[@class='title-new checkout-current']").text
print(actual_payment_title)
if actual_payment_title.__contains__(payment_title):
    print("User is in Payment Page")
else:
    print("User is not in Payment page")

driver.close()
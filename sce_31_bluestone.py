'''
Scenario 31
1. open browser
2. enter URL(blustone)
 3. click on goldmine 10+1 Sceheme
  4. enter  monthly amount and email address and click on start now
   5. fill  necessary details and click on next
   6. Fill necessary details in next page
    7. verify wheather it is navigating to payment page or not .
'''

from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.bluestone.com/")
driver.find_element_by_xpath("//li[@class='menuparent repb nav-goldmine-link']").click()
driver.find_element_by_id("amount").send_keys("1000")
driver.find_element_by_id("Email").send_keys("sujitha@gmail.com")
driver.find_element_by_id("gmsStart").click()
driver.find_element_by_id("fullname").clear()
driver.find_element_by_id("fullname").send_keys("sujithak")
driver.find_element_by_id("contactNumber").clear()
driver.find_element_by_id("contactNumber").send_keys("9000718057")
driver.find_element_by_id("address").clear()
driver.find_element_by_id("address").send_keys("sarjapura raod")
driver.find_element_by_id("postcode_delivery").clear()
driver.find_element_by_id("postcode_delivery").send_keys("562107")
driver.find_element_by_name("_eventId_savePersonalAddressDetails").click()
driver.find_element_by_id("nomineeName").clear()
driver.find_element_by_id("nomineeName").send_keys("vijay")
driver.find_element_by_name("_eventId_checkoutSaveAddressDetails").click()
act_page_url=driver.current_url
#print(act_page_url)
expe_page_url="https://www.bluestone.com/goldmineOrder?execution=e1s3"
assert act_page_url==expe_page_url,"Test Case -====Fail"
print("Payment page must be diaplayed------------pass")
driver.close()
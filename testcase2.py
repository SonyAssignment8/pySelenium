from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://localhost:8888/")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_name("user_name").send_keys("admin")
driver.find_element_by_name("user_password").send_keys("root")
driver.find_element_by_id("submitButton").click()
driver.find_element_by_link_text("Organizations").click()
driver.find_element_by_xpath("//img[contains(@title,'Create Organization...')]").click()
driver.find_element_by_name("accountname").send_keys("dell")

'''a= driver.find_element_by_xpath("//span[contains(text(),'Organization Information')]")
b=a.text
print(b)
assert b,"True"
"False"'''

driver.find_element_by_name("bill_street").send_keys("richmond road,blg")
import time
time.sleep(3)
driver.find_element_by_xpath("//input[contains(@onclick,'return copyAddressRight(EditView)')]").click()

#driver.find_element_by_name("ship_street")
#driver.find_element_by_name("button").click()
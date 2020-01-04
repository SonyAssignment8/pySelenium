'''
Scenario 26
 1. Open browser
 2. enter URL(bluestone)
 3. scroll upto some axis
 4. check whether top icon  is displayed or not
 5. if it displayed click on it 6. close browser
'''
from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.bluestone.com/")
driver.find_element_by_xpath("//a[text()='Offers ']").click()
driver.execute_script("window.scrollTo(0,5000)")
import time
time.sleep(4)
flag=driver.find_element_by_id("scrollTop").is_displayed()
print(flag)
assert flag=="scroll to top","image is not displayed"
print("image is displayed")
driver.close()
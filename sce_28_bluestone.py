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
driver.execute_script("window.scrollTo(0,5000)")
import time
time.sleep(3)
driver.find_element_by_xpath("//li[@class='menuparent repb nav-goldmine-link']").click()
act_url=driver.current_url
exp_url="https://www.bluestone.com/goldmine.html?gmfidv=GMS50"
assert act_url==exp_url,"Test case failed"
print("After scrolling also able to click the top links===pass")
driver.close()
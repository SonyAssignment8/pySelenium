'''
Scenario 29
1. open browser
2. enter URL(blustone)
3. click on goldmine 10+1 Sceheme
4. enter  monthly amount and email address and click on start now
5. verify wheather monthly amount and email address entered is reflected in next  page
 6. close browser
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
act_url=driver.current_url
print(act_url)
expec_url="https://www.bluestone.com/goldmineOrder?execution=e1s1"
assert act_url==expec_url,"Test case failed"
print("After entering details it will navigated to the next page===pass")
driver.close()
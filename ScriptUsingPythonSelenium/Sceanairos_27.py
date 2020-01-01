'''
Scenario 25
1. open Browser
2. enter URL(bluestone)
 3. go to search and search for rings
  4. go to Gender
  5. get count of women
   6. close browser
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.bluestone.com/")
driver.find_element_by_xpath("//a[text()='Rings ']").click()
import time

wb=driver.find_element_by_xpath("//section[@id='Gender-form']")
act=ActionChains(driver)
act.click_and_hold(wb).perform()
time.sleep(3)
women_count=driver.find_element_by_xpath("//span[@data-displayname='women']").text
print(women_count)
driver.close()


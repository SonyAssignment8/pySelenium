'''
Scenario 22
 1. open Browser
 2. enter URL(bluestone)
 3. go to search and search for rings
  4. move the cursor to Delivery time
  5. get the count of Next Day Delivery
  6. close browser
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.bluestone.com/")
driver.find_element_by_id("search_query_top_elastic_search").send_keys("rings")
driver.find_element_by_name("submit_search").click()
import time
time.sleep(3)
act=ActionChains(driver)
import time
time.sleep(3)
wb=driver.find_element_by_xpath("//span[text()='Delivery Time']")
act.click_and_hold(wb).perform()
nextday_count=driver.find_element_by_xpath("//span[@data-displayname='next day delivery']").text
print(nextday_count)
driver.close()
'''
Scenario 23
1. open Browser
2. enter URL(bluestone)
3. go to search and search for rings
4. move the cursor to Metal
5. get the count of Platinum
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
wb=driver.find_element_by_xpath("//span[text()='Metal']")
act.click_and_hold(wb).perform()
platinum_count=driver.find_element_by_xpath("//span[@data-displayname='platinum']").text
print(platinum_count)
driver.close()
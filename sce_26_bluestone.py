'''
Scenario 24
1. Open browser
2. enter URL(bluestone)
3. go to search and search for rings
 4. go to gold purity
 5. get count of 22k
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
driver.find_element_by_xpath("//span[@class='style-fill title']").click()
count_22k=driver.find_element_by_xpath("//span[@data-displayname='22k']").text
print(count_22k)
driver.close()
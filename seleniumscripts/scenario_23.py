from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.bluestone.com/")
driver.find_element_by_id("search_query_top_elastic_search").send_keys("rings",Keys.ENTER)
act=ActionChains(driver)
a=driver.find_element_by_xpath("//span[contains(text(),'Metal')]")
act.move_to_element(a).perform()
count=driver.find_element_by_xpath("//span[@data-displayname='platinum']")
c=count.text
print(c)

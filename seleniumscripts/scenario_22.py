from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.bluestone.com/")
driver.find_element_by_id("search_query_top_elastic_search").send_keys("rings",Keys.ENTER)
a=driver.find_element_by_xpath("//div[@id='top-filter']//span[contains(text(),'Delivery Time')]")
act=ActionChains(driver)
act.move_to_element(a).perform()
c=driver.find_element_by_xpath("//div[@class='bs-tt bs-tt-tl bs-tt-sq bs-tt-blue active']//span[contains(@data-displayname,'next day')]")
count=c.text
print(count)
c.click()
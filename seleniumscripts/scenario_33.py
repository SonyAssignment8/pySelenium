from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.bluestone.com/")
driver.find_element_by_id("search_query_top_elastic_search").send_keys("rings",Keys.ENTER)
driver.find_element_by_xpath("//div[contains(@class,'p-image')]//a[@id='pid_13840']").click()

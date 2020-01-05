from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path='C:\\Users\\kodiak\\Downloads\\chromedriver.exe')
driver.get("https://www.bluestone.com/")
driver.maximize_window()
driver.find_element_by_name("search_query").send_keys("Rings")
driver.find_element_by_name("submit_search").click()
mousehover=driver.find_element_by_xpath("//span[text()='Price']")
a=ActionChains(driver)
a.move_to_element(mousehover).perform()
driver.find_element_by_xpath("//span[text()='Rs.']").click()
a=


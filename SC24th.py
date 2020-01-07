from selenium import webdriver
import time
#1 Open browser
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
#2 Enter URL(bluestone)
driver.get("https://www.bluestone.com/")
driver.maximize_window()
driver.implicitly_wait(12)

#3 go to search and search for rings
driver.find_element_by_name("search_query").send_keys("Rings")
driver.find_element_by_xpath("//input[@name='submit_search']").click()
time.sleep(1)
#4 go to gold purity
driver.find_element_by_xpath("//span[text()='More Filters']").click()
wb_txt_22k = driver.find_element_by_xpath("//span[@data-displayname='22k']").text
print("Gold Purity Count for",wb_txt_22k)
driver.close()


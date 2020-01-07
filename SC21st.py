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

#4 move the cursor to price
act = ActionChains(driver)
wb_price = driver.find_element_by_xpath("//span[text()='Price']")
time.sleep(2)
wb_click_price = driver.find_element_by_xpath("//span[@data-displayname='below rs 10000']")
act.move_to_element(wb_price).click(wb_click_price).perform()

time.sleep(2)

wb_count = driver.find_element_by_xpath("//span[@class='total-designs']").text
print("Count:",wb_count)


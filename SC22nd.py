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
time.sleep(2)
#4 move the cursor to Delivery time
act = ActionChains(driver)
wb_deliveryTime = driver.find_element_by_xpath("//span[text()='Delivery Time']")
wb_click_delTime = driver.find_element_by_xpath("//span[@data-displayname='next day delivery']")
act.move_to_element(wb_deliveryTime).click(wb_click_delTime).perform()

#5 get the count of Next Day Delivery
wb_count = driver.find_element_by_xpath("//span[@class='total-designs']").text
print("Count:",wb_count)

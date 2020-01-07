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

#4 Click on any product
driver.find_element_by_xpath("//a[@id='pid_41483']").click()

driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
original_price = driver.find_element_by_xpath("//span[@id='our_price_display']").text
print("Actual price:",original_price)
disc_price = driver.find_element_by_xpath("//span[@class='banner-text']").text
print("Discount percentage:",disc_price)
actual_price = driver.find_element_by_xpath("//span[@id='discountedPriceSpan']").text
print("Actual Price:",actual_price)



#//span[@id='our_price_display']
'''Scenario 33
1. open browser
2. enter url(bluestone)
3. search for rings
4. click on any product
5. verify original price discount price and actual price '''
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome("./chromedriver.exe")
#Navigate to bluestone page
driver.get("https://www.bluestone.com/")
driver.maximize_window()
#search for rings
driver.find_element_by_name("search_query").send_keys("rings")
driver.find_element_by_xpath("//input[@name='submit_search']").click()

#click on any product
driver.find_element_by_xpath("//img[@alt='The Aaradh Band for Him']").click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
Actual_price=driver.find_element_by_xpath("//div[@class='price-inner']").text
discount_price=driver.find_element_by_xpath("//span[@id='our_price_display']").text
print("Actual price:",Actual_price)
print("Discounted price:",discount_price)
driver.close()


'''Scenario 22
 1. open Browser
 2. enter URL(bluestone)
 3. go to search and search for rings
 4. move the cursor to Delivery time
 5. get the count of Next Day Delivery
 6. close browser
 '''
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome("./chromedriver.exe")
#Navigate to bluestone page
driver.get("https://www.bluestone.com/")
driver.maximize_window()
#go to search and search for rings
driver.find_element_by_name("search_query").send_keys("rings")
driver.find_element_by_xpath("//input[@value='Search']").click()
time.sleep(6)
driver.execute_script("window.scrollBy(0,1000)")
#move the cursor to Delivery time
element=driver.find_element_by_xpath("//span[text()='Delivery Time']")
act=ActionChains(driver)
act.click_and_hold(element).perform()
#get the count of Next Day Delivery
count_item=driver.find_element_by_xpath("(//span[text()=' Next Day Delivery '])").text
print("The count of Next Day Delivery is :",count_item[18: :])
driver.close()
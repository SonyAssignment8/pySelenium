'''Scenario 23
1. open Browser
2. enter URL(bluestone)
3. go to search and search for rings
4. move the cursor to Metal
5. get the count of Platinum
6. close browser '''
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
#move the cursor to Metal
metal=driver.find_element_by_xpath("//span[text()='Metal']")
platinum=driver.find_element_by_xpath("//span[text()=' Platinum ']")
time.sleep(5)
act=ActionChains(driver)
act.move_to_element(metal).click_and_hold(platinum).perform()
time.sleep(5)
#Get the count of platinum
count=driver.find_element_by_xpath("//span[text()=' Platinum ']").text
print("The count of platinum is :",count[9: :])
driver.close()


'''Scenario 21
1. open Browser
2. enter URL(bluestone)
3. go to search and search for rings
4. move the cursor to price
5. get the count of below 10000 Rs
6. close browser Scenario '''
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
#move the cursor to price
act=ActionChains(driver)
price=driver.find_element_by_xpath("//span[text()='Price']")
#get the count of below 10000 Rs
price_click=driver.find_element_by_xpath("//span[@data-displayname='below rs 10000']")
act.move_to_element(price).click(price_click).perform()
time.sleep(4)
count=driver.find_element_by_xpath("//span[@class='total-designs']").text
print(count[0:2: ])
driver.close()

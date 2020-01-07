'''Scenario 25
1. open Browser
2. enter URL(bluestone)
3. go to search and search for rings
4. go to Gender
5. get count of women
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
driver.execute_script("window.scrollBy(0,1000)")
time.sleep(4)
#go to Gender
act=ActionChains(driver)
ring=driver.find_element_by_xpath("//span[text()='Gender']")
women=driver.find_element_by_xpath("//span[@data-displayname='women']")
act.move_to_element(ring).click_and_hold(women).perform()
time.sleep(4)
#Get the count
count=women.text
print("Count of the women rings:",count[6::])
driver.close()
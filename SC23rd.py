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

#4 move the cursor to Metal
act = ActionChains(driver)
wb_metal = driver.find_element_by_xpath("//span[text()='Metal']")
wb_platinum_count = driver.find_element_by_xpath("//div[@class='form-item last']/span[@data-displayname='platinum']")
act.move_to_element(wb_metal).perform()
plt = wb_platinum_count.text
print("Count of Platinum rings:",plt[8::])
driver.close()
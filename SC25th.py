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
#4 go to Gender
act = ActionChains(driver)
wb_gender = driver.find_element_by_xpath("//span[text()='Gender']")
time.sleep(2)
wb_gender_women = driver.find_element_by_xpath("//span[@data-displayname='women']")
act.move_to_element(wb_gender).click(wb_gender_women).perform()

#5 get count of women
wb_count = driver.find_element_by_xpath("//span[@class='total-designs']").text
print("Total Woman Count:",wb_count)
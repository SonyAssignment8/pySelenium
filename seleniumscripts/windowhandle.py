from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.find_element_by_xpath("//button[text()='✕']").click()
parentsid=driver.current_window_handle
driver.find_element_by_name("q").send_keys("tv")
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(3)
driver.find_element_by_xpath("//div[contains(text(),'Micromax 81cm (32 inch) HD Ready LED Smart Android TV')]").click()
childsid=driver.window_handles[1]
driver.switch_to.window(childsid)
cost=driver.find_element_by_xpath("//div[text()='₹9,999']").text
print(cost)


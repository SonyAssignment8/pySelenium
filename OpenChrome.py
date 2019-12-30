from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://selenium.dev/")

driver.fullscreen_window() # to open browser in fullscreen mode
driver.minimize_window()
driver.maximize_window()
driver.back()
driver.forward()
str = driver.title
print(str)
print(driver.current_url)
driver.refresh()
driver.close()

#driver.implicitly_wait(5)
#driver.find_elements_by_link_text("download").click()
#driver.find_element_by_xpath("//div[@class='download-button ide']").click()
driver.find_element_by_xpath("//h3[@class='ide-header']/following-sibling::div").click()


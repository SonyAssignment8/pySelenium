import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.bluestone.com/")
driver.maximize_window()

# Move the cursor All Jewellery
all_jewel = driver.find_element_by_xpath("//a[@title='Jewellery']")
act = ActionChains(driver)
act.move_to_element(all_jewel).perform()

# select Kadas and click on it
driver.find_element_by_xpath("//span[text()='Kadas']").click()

# select any kada.
driver.find_element_by_xpath("//img[@alt='The Alok Kada For Him']").click()

# click on 'buy now'
child_win = driver.window_handles[1]
driver.switch_to.window(child_win)
driver.find_element_by_id("buy-now").click()

# Capture whether error message is displayed or not
exp_error_msg = '* This field is required'
act_error_msg = driver.find_element_by_xpath("//div[@class='formErrorContent']").text
assert exp_error_msg == act_error_msg, "Error message not displayed"
print("Error message is displayed")

# close the browser
driver.close()

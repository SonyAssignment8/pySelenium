import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://www.bluestone.com/")
driver.maximize_window()

# Goto chat our experts
driver.switch_to_frame("chat-widget")
driver.find_element_by_xpath("//p[text()='CHAT with our experts !']").click()

# Enter the details and click on start chat
driver.find_element_by_id("name").send_keys("Jyoti Sahu")
driver.find_element_by_id("email").send_keys("jyoti08.sahu@gmail.com")
driver.find_element_by_id("name_146917605549304831").send_keys('7587149823')

# Click on start chat now
driver.find_element_by_xpath("//span[text()='Start the chat']").click()
print("Chat started")

# close the browser
driver.close()
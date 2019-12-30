import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://www.bluestone.com/")
driver.maximize_window()

# Click on offers
driver.find_element_by_xpath("//a[@title='Offers']").click()

# Select 0% off Making charge and click on it
driver.find_element_by_xpath("//span[@data-displayname='20% making charge off']").click()

# Click on start chat now
driver.find_element_by_xpath("//span[text()='Start the chat']").click()
print("Chat started")

# close the browser
driver.close()
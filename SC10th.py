from selenium import webdriver
import time
#1 Open browser
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
#2 Enter URL(bluestone)
driver.get("https://www.bluestone.com/")
driver.maximize_window()
time.sleep(8)
#3 Goto chat our experts and maximize
driver.switch_to_frame("chat-widget")
time.sleep(4)
driver.find_element_by_xpath("//p[text()='CHAT with our experts !']").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@name='name']").send_keys("Akshay")
driver.find_element_by_xpath("//input[@name='email']").send_keys("ak@gmail.com")
driver.find_element_by_xpath("//input[@name='name_146917605549304831']").send_keys("1234567890")
driver.find_element_by_xpath("//span[text()='Start the chat']").click()
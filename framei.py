from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.bluestone.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.switch_to_frame("chat-widget")
#driver.switch_to.frame("chat-widget")
time.sleep(30)
driver.find_element_by_xpath("//p[text()='CHAT with our experts !']").click()
time.sleep(10)
driver.find_element_by_id("name").send_keys("Ankita")
driver.find_element_by_name("email").send_keys("abc@gmail.com")
driver.find_element_by_name("name_146917605549304831").send_keys("8765439023")
#driver.find_element_by_xpath("//span[text()='Start the chat']").click()
time.sleep(20)
driver.switch_to.default_content()
#driver.close()
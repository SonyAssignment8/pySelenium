'''Scenario 10
1. Open browser
2. Pass url bluestone
3. Goto chat our experts and maximize
4. Maxmize chat our experts
5. Enter the details and click on start chat
6. Enter some message.
7. And print reply in output Scenario '''
import time

from selenium import webdriver
driver=webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.bluestone.com/")
time.sleep(8)
driver.switch_to_frame("chat-widget")
time.sleep(4)
driver.find_element_by_xpath("//p[text()='CHAT with our experts !']").click()
time.sleep(4)
driver.find_element_by_id("name").send_keys("Divya")
driver.find_element_by_id("email").send_keys("deepuravishancar@gmail.com")
driver.find_element_by_id("name_146917605549304831").send_keys("purchase")
driver.find_element_by_xpath("//span[text()='Start the chat']").click()
print(driver.find_element_by_xpath("//span[@class='Linkify']").text)

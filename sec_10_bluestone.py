'''
Scenario 10
1. Open browser
2. Pass url bluestone
3. Goto chat our experts and maximize
4. Maxmize chat our experts
5. Enter the details and click on start chat
6. Enter some message.
7. And print reply in output
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.bluestone.com/")
import time
time.sleep(6)
driver.switch_to.frame("chat-widget")
time.sleep(3)
driver.find_element_by_xpath("//p[contains(text(),'CHAT with our experts !')]").click()
driver.find_element_by_id("name").send_keys("sujitha")
driver.find_element_by_id("email").send_keys("sujitha@gmail.com")
driver.find_element_by_id("name_146917605549304831").send_keys("9000718057")
driver.find_element_by_xpath("//span[contains(text(),'Start the chat')]").click()
reply_text=driver.find_element_by_xpath("//div[@class='lc-12rycc2 e1v4xcti0']").text
print(reply_text)

time.sleep(5)
driver.switch_to_default_content()
ring_we=driver.find_element_by_xpath("//a[@title='Offers']")
act=ActionChains(driver)
act.click_and_hold(ring_we).perform()
driver.find_element_by_xpath("//span[contains(text(),'20% off on making charge')]").click()
time.sleep(5)
driver.quit()

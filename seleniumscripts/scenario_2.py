from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("http://webmail.testyantra.in/")
time.sleep(2)
driver.find_element_by_id("user").send_keys("rashmi.n@testyantra.in")
time.sleep(2)
driver.find_element_by_id("pass").send_keys("softwaretest")
driver.find_element_by_id("login_submit").click()
time.sleep(2)

frame=driver.find_element_by_id("mailFrame")
driver.switch_to_frame(frame)
driver.find_element_by_link_text("New Message").click()
act_title=driver.title
exp_title="Webmail - Main"
if act_title.__contains__(exp_title):
    print("pass")
else:
    print("fail")

childsid=driver.window_handles[1]
driver.switch_to_window(childsid)
time.sleep(2)
driver.find_element_by_xpath("//input[@class='hordeACTrigger impACTrigger']").send_keys("krishna.k@testyantra.in")
driver.find_element_by_id("subject").send_keys("Test Mail")
driver.find_element_by_id("composeMessage").send_keys("Hi...")
time.sleep(4)
driver.find_element_by_id("send_button").click()
#driver.close()
from selenium import webdriver
import autoit
import time
driver = webdriver.Chrome()
driver.get("http://webmail.testyantra.in/cpsess4343257689/webmail/paper_lantern/index.html?login=1&post_login=41798576748722")
driver.maximize_window()
driver.find_element_by_name("user").send_keys("ankita.m@testyantra.in")
#driver.find_element_by_xpath("//span[text()='Next']").click()

driver.find_element_by_id("pass").send_keys("Ankita77$")
driver.find_element_by_name("login").click()
driver.implicitly_wait(20)

fr=driver.find_element_by_id("mailFrame")
driver.switch_to.frame(fr)
par=driver.window_handles[0]
driver.find_element_by_link_text("New Message").click()
child=driver.window_handles[1]
driver.switch_to.window(child)
driver.maximize_window()
driver.find_element_by_xpath("//input[@class='hordeACTrigger impACTrigger']").send_keys("more.ankita77@yahoo.com")
driver.find_element_by_id("subject").send_keys("leave")
driver.find_element_by_name("message").send_keys("hi hello ankita")
driver.find_element_by_xpath("//label[text()='Add Attachment']").click()
print(len(driver.window_handles))
time.sleep(10)
autoit.win_wait("Open",3)
autoit.control_send("Open","Edit1","db.json")
time.sleep(3)
autoit.control_click("Open","Button1")

driver.find_element_by_id("send_button").click()
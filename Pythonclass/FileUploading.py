# import autoit
# #this code is for file uploading
# autoit.win_wait_active("[CLASS:#32770]",3)
# autoit.control_send("[CLASS:#32770]","Edit1","Emails.csv")
# autoit.control_click("[CLASS:#32770]","Button1")
#
# #code for file downloading
# autoit.win_wait_active("[MozillaDialogClass]",3)
# autoit.control_send("!S")
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://gmail.com")
driver.find_element_by_id("identifierId").send_keys("htkrishnakumara")
driver.find_element_by_xpath("//span[text()='Next']").click()
time.sleep(5)
driver.find_element_by_name("password").send_keys("Krishna@123")
driver.find_element_by_xpath("//span[text()='Next']").click()
time.sleep(5)
driver.find_element_by_xpath("//div[text()='Compose']").click()
time.sleep(3)
driver.find_element_by_xpath("//div[@class='a1 aaA aMZ']").click()
import autoit
autoit.win_wait("Open",3)
autoit.auto_it_set_option("Open","Edit2","gk.docx")
autoit.control_click("Open","Button1")

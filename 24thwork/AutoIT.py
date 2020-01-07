import autoit
from selenium import webdriver
import time
driver=webdriver.Chrome("./chromedriver.exe")
driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_name("identifier").send_keys("selenium658@gmail.com")
driver.find_element_by_xpath("//span[text()='Next']").click()
driver.find_element_by_name("password").send_keys("deepu@0109")
time.sleep(3)
driver.find_element_by_xpath("//span[text()='Next']").click()
driver.find_element_by_xpath("//div[text()='Compose']").click()
autoit.win_wait_active("[CLASS:#32770]",3)
autoit.control_send("[CLASS:#32770]","Edit","exception.txt")
autoit.control_click("[CLASS:#32770]","Button")
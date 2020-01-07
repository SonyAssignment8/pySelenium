from selenium import webdriver
import time
#1 Open browser
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
#2 Enter URL(yatra)
driver.get("https://www.yatra.com/")
driver.maximize_window()
driver.implicitly_wait(12)
time.sleep(2)
driver.find_element_by_xpath("//input[@name='flight_origin']").click()
time.sleep(1)
driver.find_element_by_xpath("//p[@class='ac_cityname']").send_keys("Bangalore")
time.sleep(1)
driver.find_element_by_xpath("//input[@name='flight_destination']").clear()

driver.find_element_by_xpath("//input[@name='flight_destination']").send_keys("Himachal")


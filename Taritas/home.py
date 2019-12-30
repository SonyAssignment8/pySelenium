from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.google.com/")
time.sleep(10)
driver.maximize_window()
driver.execute_script('window.open(("http://www.taritas.com/"),"tab2")')
time.sleep(10)
driver.switch_to_window("tab2")
driver.find_element_by_xpath("//li[@class='active']/a[text()='Home']").click()
# driver.find_element_by_xpath("//li[@class='active']/a[text()='About Us']").click()
time.sleep(10)
driver.find_element_by_xpath("(//a[contains(text(),'About')])[1]").click()


from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://webmail.testyantra.in")
driver.maximize_window()
driver.find_element_by_name("user").send_keys("sujitha.k@testyantra.in")
driver.find_element_by_name("pass").send_keys("kondavkr@484")
driver.find_element_by_name("login").click()
driver.find_element_by_xpath("//a[@class='horde-mainnavi-active']")

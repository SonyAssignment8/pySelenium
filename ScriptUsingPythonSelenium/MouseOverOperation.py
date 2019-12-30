from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.craftvilla.com")
driver.implicitly_wait(10)
mouseovr=driver.find_elements_by_xpath("//")
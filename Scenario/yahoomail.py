from selenium import webdriver
driver=webdriver.Chrome("./chromedriver.exe")
driver.get("https://login.yahoo.com")
driver.find_elements_by_id("login-username").send_keys("divya_ravishankar")
driver.find_elements_by_id("login-signin").click()
driver.find_element_by_id("login-passwd").send_keys("deepu@0109")
driver.find_elements_by_id("login-signin").click()
driver.find_elements_by_xpath("//span[text()='Mail']").click()
driver.find
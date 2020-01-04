from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.bluestone.com/")
privacy=driver.find_element_by_xpath("//span[text()='Write to us']")
driver.execute_script("arguments[0].scrollIntoView();",privacy)
privacy.click()
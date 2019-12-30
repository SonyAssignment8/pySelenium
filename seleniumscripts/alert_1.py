from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://javascript.info/alert-prompt-confirm")
driver.find_element_by_xpath("//a[contains(text(),'Run the demo')]").click()
driver.switch_to_alert().send_keys("rashmi")
driver.switch_to_alert().accept()
print(driver.switch_to_alert().text)
driver.switch_to_alert().accept()
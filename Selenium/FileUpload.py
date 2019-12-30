from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.naukri.com/")
driver.find_element_by_id("input_resumeParser").click()
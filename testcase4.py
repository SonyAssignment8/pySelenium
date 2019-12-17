from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://localhost:8888/")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_name("user_name").send_keys("admin")
driver.find_element_by_name("user_password").send_keys("root")
driver.find_element_by_id("submitButton").click()
driver.find_element_by_link_text("Organizations").click()
#driver.find_element_by_xpath("//img[contains(@title,'Create Organization...')]").click()
#driver.find_element_by_xpath("//a[@title='Organizations']").click()
driver.find_element_by_xpath("//input[@name='selected_id']").click()
driver.find_element_by_xpath("//input[@class='crmbutton small delete']").click()
alert1=driver.switch_to.alert
alert1.accept()

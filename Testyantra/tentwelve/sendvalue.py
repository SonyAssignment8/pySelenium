from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\Python\chromedriver.exe")
driver.get("https://demo.actitime.com/login.do")
driver.maximize_window()
driver.find_element_by_id("username")
driver.find_element_by_id("username").send_keys("Vishwakarmaatul11@gmail.com")
driver.find_element_by_id("password")
driver.find_element_by_id("password").send_keys("9981042157")
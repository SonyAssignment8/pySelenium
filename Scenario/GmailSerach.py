from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\Python\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
# driver.find_element_by_id("//input[@id='fakebox-input']").send_keys("gmail")
driver.find_element_by_class_name("gb_g").click()
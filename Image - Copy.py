from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\Python\chromedriver.exe")
driver.get("https://www.linkedin.com/login")
driver.maximize_window()
driver.find_element_by_tag_name("img")



driver.quit()